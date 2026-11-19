"""Render every solution.<lang>.bpmn to solution.<lang>.svg with bpmn-js in headless Chromium.

Usage: python tools/render_svg.py [--viewer PATH_TO_bpmn-viewer.production.min.js]
Needs: pip install playwright && playwright install chromium. Without --viewer the bpmn-js viewer is loaded from unpkg.
"""

import argparse
import functools
import http.server
import shutil
import tempfile
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

CORPUS = Path(__file__).resolve().parents[1]
CDN = "https://unpkg.com/bpmn-js@17.11.1/dist/bpmn-viewer.production.min.js"
PAGE = """<!doctype html><meta charset="utf-8"><div id="c" style="width:1600px;height:900px"></div>
<script src="{js}"></script><script>
window.render = async (xml) => {{ const v = new BpmnJS({{container: '#c'}}); await v.importXML(xml);
  const {{svg}} = await v.saveSVG(); v.destroy(); return svg; }};
</script>"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--viewer", help="local bpmn-viewer.production.min.js")
    args = ap.parse_args()
    tmp = Path(tempfile.mkdtemp())
    js = CDN
    if args.viewer:
        shutil.copy(args.viewer, tmp / "viewer.js")
        js = "viewer.js"
    (tmp / "index.html").write_text(PAGE.format(js=js), encoding="utf-8")
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(tmp))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    files = sorted(CORPUS.glob("exercises/*/solution.*.bpmn")) + sorted(CORPUS.glob("assessment/*/solution.*.bpmn"))
    files += sorted(CORPUS.glob("exams/*/Q*/v*/*.bpmn"))
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"http://127.0.0.1:{server.server_port}/index.html")
        page.wait_for_function("typeof window.BpmnJS === 'function'")
        for f in files:
            svg = page.evaluate("xml => window.render(xml)", f.read_text(encoding="utf-8"))
            f.with_suffix(".svg").write_text(svg, encoding="utf-8")
        browser.close()
    server.shutdown()
    print(f"{len(files)} diagrams rendered")


if __name__ == "__main__":
    main()
