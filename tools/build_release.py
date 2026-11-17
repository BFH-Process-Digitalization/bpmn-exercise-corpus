"""Build the readable release files from exercise.yaml and the rendered SVGs.

Writes per exercise exercise.de.md and exercise.en.md, the index index.csv and the booklets
booklet/exercises-de.html / -en.html. With --pdf the booklets are also printed to PDF (needs playwright).
Run render_svg.py first.

Usage: python tools/build_release.py [--pdf]
"""

import argparse
import csv
import html
from pathlib import Path

import yaml

CORPUS = Path(__file__).resolve().parents[1]
TOPICS = {
    1: ("Aktivitäten", "Activities"),
    2: ("Gateways und Parallelität", "Gateways and parallelism"),
    3: ("Ereignisse", "Events"),
    4: ("Kollaboration", "Collaboration"),
    5: ("Daten und Artefakte", "Data and artifacts"),
    6: ("Ausnahmen und Kompensation", "Exceptions and compensation"),
}
T = {
    "de": {
        "level": {"basic": "Grundlagen", "advanced": "Fortgeschritten"},
        "task": "Aufgabe",
        "goal": "Lernziel",
        "elements": "Elemente",
        "time": "Zeit",
        "minutes": "Minuten",
        "core": "Kernaufgabe",
        "mistakes": "Typische Fehler",
        "solution": "Musterlösung",
        "topic": "Thema",
        "booklet": "BPMN-Übungen mit Musterlösungen",
        "pre": "Vortest",
        "licence": "Lizenz: CC BY 4.0",
    },
    "en": {
        "level": {"basic": "Basic", "advanced": "Advanced"},
        "task": "Task",
        "goal": "Learning goal",
        "elements": "Elements",
        "time": "Time",
        "minutes": "minutes",
        "core": "Core exercise",
        "mistakes": "Typical mistakes",
        "solution": "Sample solution",
        "topic": "Topic",
        "booklet": "BPMN exercises with sample solutions",
        "pre": "Pre-test",
        "licence": "Licence: CC BY 4.0",
    },
}
ORDER = ["B", "B2", "B3", "A", "A2", "A3"]


def load():
    items = []
    for f in sorted(CORPUS.glob("exercises/*/exercise.yaml")):
        items.append((f.parent, yaml.safe_load(f.read_text(encoding="utf-8"))))
    items.sort(key=lambda x: (x[1]["topic"], ORDER.index(x[1]["slot"])))
    return items


def heading(m, lang):
    t = T[lang]
    if m["id"] == "PRE":
        return f"{t['pre']}: {m['title'][lang]}"
    return f"{m['id']} {m['title'][lang]}"


def markdown(d: Path, m: dict, lang: str) -> str:
    t = T[lang]
    meta = []
    if m.get("topic"):
        meta.append(
            f"{t['topic']} {m['topic']}: {TOPICS[m['topic']][0 if lang == 'de' else 1]}, {t['level'][m['level']]}"
        )
    meta.append(
        f"{t['time']}: {m['time_limit_minutes']} {t['minutes']}"
        + (f", {t['core']}" if m.get("core") and m.get("topic") else "")
    )
    mistakes = "\n".join(f"- {x[lang]}" for x in m["expected_mistakes"])
    return (
        f"# {heading(m, lang)}\n\n{' | '.join(meta)}\n\n## {t['task']}\n\n{' '.join(m['text'][lang].split())}\n\n"
        f"## {t['goal']}\n\n{m['learning_goal'][lang]}\n\n{t['elements']}: {m['elements']}\n\n"
        f"## {t['solution']}\n\n![{t['solution']}](solution.{lang}.svg)\n\nBPMN: [solution.{lang}.bpmn](solution.{lang}.bpmn)\n\n"
        f"## {t['mistakes']}\n\n{mistakes}\n\n---\n{t['licence']}\n"
    )


def booklet(items, lang: str) -> str:
    t = T[lang]
    parts = [f"<h1>{t['booklet']}</h1><p>{t['licence']}</p>"]
    for d, m in items:
        svg = (d / f"solution.{lang}.svg").read_text(encoding="utf-8") if (d / f"solution.{lang}.svg").exists() else ""
        mistakes = "".join(f"<li>{html.escape(x[lang])}</li>" for x in m["expected_mistakes"])
        meta = html.escape(markdown(d, m, lang).split("\n")[2])
        parts.append(
            f'<section class="ex"><h2>{html.escape(heading(m, lang))}</h2><p class="meta">{meta}</p>'
            f"<h3>{t['task']}</h3><p>{html.escape(' '.join(m['text'][lang].split()))}</p>"
            f"<h3>{t['goal']}</h3><p>{html.escape(m['learning_goal'][lang])}</p></section>"
            f'<section class="sol"><h3>{t["solution"]}: {html.escape(m["id"])}</h3><div class="svg">{svg}</div>'
            f"<h3>{t['mistakes']}</h3><ul>{mistakes}</ul></section>"
        )
    css = (
        "body{font-family:Helvetica,Arial,sans-serif;font-size:11pt;margin:0} h1{font-size:20pt} h2{font-size:15pt}"
        " .ex,.sol{page-break-after:always} .meta{color:#555} .svg svg{max-width:100%;height:auto;max-height:150mm}"
        " @page{size:A4 landscape;margin:15mm}"
    )
    return f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><title>{t["booklet"]}</title><style>{css}</style><body>{"".join(parts)}</body></html>'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true")
    args = ap.parse_args()
    items = load()
    pre = CORPUS / "assessment" / "PRE"
    all_items = items + [(pre, yaml.safe_load((pre / "exercise.yaml").read_text(encoding="utf-8")))]
    for d, m in all_items:
        for lang in ("de", "en"):
            (d / f"exercise.{lang}.md").write_text(markdown(d, m, lang), encoding="utf-8")
    with open(CORPUS / "index.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(
            [
                "id",
                "topic",
                "level",
                "slot",
                "core",
                "time_limit_minutes",
                "sector",
                "title_de",
                "title_en",
                "elements",
                "folder",
            ]
        )
        for d, m in all_items:
            w.writerow(
                [
                    m["id"],
                    m.get("topic") or "",
                    m.get("level") or "",
                    m.get("slot") or "",
                    m.get("core"),
                    m["time_limit_minutes"],
                    m["sector"],
                    m["title"]["de"],
                    m["title"]["en"],
                    m["elements"],
                    d.relative_to(CORPUS).as_posix(),
                ]
            )
    out = CORPUS / "booklet"
    out.mkdir(exist_ok=True)
    for lang in ("de", "en"):
        (out / f"exercises-{lang}.html").write_text(booklet(all_items, lang), encoding="utf-8")
    if args.pdf:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            for lang in ("de", "en"):
                page.goto((out / f"exercises-{lang}.html").as_uri())
                page.pdf(path=str(out / f"exercises-{lang}.pdf"), format="A4", landscape=True, print_background=True)
            browser.close()
    print(f"{len(all_items)} exercises written")


if __name__ == "__main__":
    main()
