"""Build exam pages and sheets from exams/*/Q*/.

Writes question.de.md / question.en.md per variant and, per level and version A to E (variant 1 to 5 of every question),
an exam sheet and a solution sheet as HTML in exams/sheets/. With --pdf the sheets are also printed to PDF (needs playwright).
Run render_svg.py first.

Usage: python tools/build_exams.py [--pdf]
"""
import argparse, html
from pathlib import Path
import yaml

CORPUS = Path(__file__).resolve().parents[1]
EXAMS = CORPUS / "exams"
VERSIONS = "ABCDE"
T = {
 "de": dict(basic="Basic-Prüfung", advanced="Advanced-Prüfung", version="Version", solution="Lösung", task="Aufgabe", points="Punkte",
            minutes="Minuten", model="Modell", rubric="Bewertung", fault="Fehler", fix="Korrektur", key="Lösungsschlüssel",
            name="Studien-ID", total="Total", sheet="Prüfungsbogen", solsheet="Lösungsbogen", sector="Branche",
            q1="Wissensfragen (je 1 Punkt, eine Antwort ist richtig)", q2="Fehler finden und korrigieren", q3="Modellieren", q4="Modellieren",
            draw="Zeichnen Sie das Modell auf ein separates Blatt oder im Modellierungswerkzeug."),
 "en": dict(basic="Basic exam", advanced="Advanced exam", version="Version", solution="Solution", task="Task", points="points",
            minutes="minutes", model="Model", rubric="Scoring", fault="Error", fix="Fix", key="Answer key",
            name="Study ID", total="Total", sheet="Exam sheet", solsheet="Solution sheet", sector="Industry",
            q1="Knowledge items (1 point each, one answer is correct)", q2="Find and fix errors", q3="Modelling", q4="Modelling",
            draw="Draw the model on a separate sheet or in the modelling tool."),
}


def load(level):
    items = yaml.safe_load((EXAMS / level / "Q1" / "items.yaml").read_text(encoding="utf-8"))["items"]
    qs = {}
    for f in sorted((EXAMS / level).glob("Q*/v*/question.yaml")):
        m = yaml.safe_load(f.read_text(encoding="utf-8")); qs[(m["question"], m["variant"])] = (f.parent, m)
    return items, qs


def rubric_md(m, l, t):
    if "faults" in m:
        return "\n".join(f"{i}. {f[l]} **{t['fix']}:** {f['fix_' + l]} ({f['points']} {t['points']})" for i, f in enumerate(m["faults"], 1)) + f"\n\n{m['scoring'][l]}\n"
    return "| " + t["points"] + " | " + t["rubric"] + " |\n|---|---|\n" + "\n".join(f"| {r['points']} | {r[l]} |" for r in m["rubric"]) + "\n"


def markdown(d, m, l):
    t = T[l]
    s = f"# {m['id']}: {m['title'][l]}\n\n{t[m['level']]}, {m['question']}, {t['version']} {VERSIONS[m['variant'] - 1]} · {m['points']} {t['points']} · {m['time_minutes']} {t['minutes']} · {t['sector']}: {m['sector']}\n\n"
    s += f"## {t['task']}\n\n{' '.join(m['text'][l].split())}\n\n"
    if "model" in m:
        s += f"{m['task'][l]}\n\n![{t['model']}](model.{l}.svg)\n\nBPMN: [model.{l}.bpmn](model.{l}.bpmn)\n\n"
    s += f"## {t['solution']}\n\n![{t['solution']}](solution.{l}.svg)\n\nBPMN: [solution.{l}.bpmn](solution.{l}.bpmn)\n\n## {t['rubric']}\n\n" + rubric_md(m, l, t)
    return s


def svg(d, name):
    p = d / name
    return f'<div class="svg">{p.read_text(encoding="utf-8")}</div>' if p.exists() else ""


def sheet(level, v, items, qs, l, solution):
    t, e = T[l], html.escape
    head = f"{t[level]} · {t['version']} {VERSIONS[v - 1]} · {t['solsheet'] if solution else t['sheet']}"
    out = [f"<h1>{e(head)}</h1>"]
    total = 8 + sum(qs[(q, v)][1]["points"] for q in ("Q2", "Q3", "Q4"))
    mins = 8 + sum(qs[(q, v)][1]["time_minutes"] for q in ("Q2", "Q3", "Q4"))
    if not solution:
        out.append(f'<p class="meta">{mins} {t["minutes"]} · {total} {t["points"]}</p><p>{t["name"]}: ________________</p>')
    sel = sorted((it for it in items if it["variant"] == v), key=lambda it: it["slot"])
    out.append(f"<h2>Q1 {t['q1']} (8 {t['points']})</h2><ol class=q1>")
    for it in sel:
        opts = "".join(f"<li{' class=key' if solution and k == it['key'] else ''}>{e(o)}</li>" for k, o in enumerate(it[l]["options"]))
        out.append(f"<li>{e(it[l]['stem'])}<ol type=a>{opts}</ol></li>")
    out.append("</ol>")
    for q in ("Q2", "Q3", "Q4"):
        d, m = qs[(q, v)]
        out.append(f'<h2 class="pb">{q} {t[q.lower()]}: {e(m["title"][l])} ({m["points"]} {t["points"]})</h2><p>{e(" ".join(m["text"][l].split()))}</p>')
        if "model" in m:
            out.append(f"<p><b>{e(m['task'][l])}</b></p>" + svg(d, f"model.{l}.svg"))
        elif not solution:
            out.append(f"<p><i>{t['draw']}</i></p>")
        if solution:
            out.append(svg(d, f"solution.{l}.svg"))
            if "faults" in m:
                out.append("<ol>" + "".join(f"<li>{e(f[l])} <b>{t['fix']}:</b> {e(f['fix_' + l])} ({f['points']})</li>" for f in m["faults"]) + f"</ol><p>{e(m['scoring'][l])}</p>")
            else:
                out.append("<table>" + "".join(f"<tr><td>{r['points']}</td><td>{e(r[l])}</td></tr>" for r in m["rubric"]) + "</table>")
    css = ("body{font-family:Arial,sans-serif;font-size:10.5pt;margin:12mm} h1{font-size:15pt} h2{font-size:12pt;margin-top:8mm}"
           " .pb{page-break-before:always} .meta{color:#555} ol.q1{columns:2;column-gap:10mm} ol.q1>li{break-inside:avoid;margin-bottom:2mm} li.key{font-weight:bold;text-decoration:underline}"
           " .svg svg{max-width:100%;height:auto;max-height:120mm} table{border-collapse:collapse} td{border:1px solid #999;padding:2px 6px;vertical-align:top}")
    return f'<!doctype html><html lang="{l}"><meta charset="utf-8"><title>{e(head)}</title><style>{css}</style><body>{"".join(out)}</body></html>'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--pdf", action="store_true"); args = ap.parse_args()
    out = EXAMS / "sheets"; out.mkdir(exist_ok=True)
    pages = []
    for level in ("basic", "advanced"):
        items, qs = load(level)
        for (q, v), (d, m) in qs.items():
            for l in ("de", "en"):
                (d / f"question.{l}.md").write_text(markdown(d, m, l), encoding="utf-8")
        for v in range(1, 6):
            for l in ("de", "en"):
                for sol in (False, True):
                    p = out / f"{level}-{VERSIONS[v - 1]}-{'solution' if sol else 'exam'}.{l}.html"
                    p.write_text(sheet(level, v, items, qs, l, sol), encoding="utf-8"); pages.append(p)
    if args.pdf:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page()
            for p in pages:
                pg.goto(p.as_uri()); pg.pdf(path=str(p.with_suffix(".pdf")), format="A4", landscape=True, print_background=True)
            b.close()
        for p in pages: p.unlink()
    print(f"{len(pages)} sheets written")


if __name__ == "__main__":
    main()
