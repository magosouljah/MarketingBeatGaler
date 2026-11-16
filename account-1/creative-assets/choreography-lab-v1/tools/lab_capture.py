"""Deterministic stills + ground-truth geometry for the Choreography Lab.

Serves ../hyperframes statically, opens it in headless Chrome (software WebGL),
seeks with window.__lab.render(t) and either saves PNG stills or dumps the
exact projected card corners / camera distances from window.__lab.sample(t).
This is a QA helper; the delivery renders come from `hyperframes render`.

    python tools/lab_capture.py stills  OUT_DIR --variants a,b,c --at 0.3,1,2
    python tools/lab_capture.py geometry OUT.json --variants a,b,c --fps 30
Requires: playwright (Python) and a Chrome/Chromium (CHROME env or /usr/bin/google-chrome).
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import os
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1] / "hyperframes"
DURATION = 6.0


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve():
    handler = functools.partial(Quiet, directory=str(ROOT))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def open_lab(browser, port, variant):
    page = browser.new_page(viewport={"width": 720, "height": 1280})
    page.goto(f"http://127.0.0.1:{port}/index.html?variant={variant}")
    page.wait_for_function("window.__lab !== undefined", timeout=120000)
    return page


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["stills", "geometry"])
    ap.add_argument("out", type=Path)
    ap.add_argument("--variants", default="a,b,c")
    ap.add_argument("--at", default="0.3,1,2,3,3.7,4.3,5,5.9")
    ap.add_argument("--fps", type=float, default=30.0)
    a = ap.parse_args(argv)
    httpd = serve()
    port = httpd.server_address[1]
    chrome = os.environ.get("CHROME", "/usr/bin/google-chrome")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome, args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
        result = {}
        for v in a.variants.split(","):
            page = open_lab(browser, port, v)
            if a.mode == "stills":
                a.out.mkdir(parents=True, exist_ok=True)
                for t in [float(x) for x in a.at.split(",")]:
                    page.evaluate(f"window.__lab.render({t})")
                    page.locator("#stage").screenshot(path=str(a.out / f"{v}-{t:05.2f}.png"))
            else:
                n = int(round(DURATION * a.fps))
                times = [i / a.fps for i in range(n)]
                result[v] = {
                    "label": page.evaluate("window.__lab.label"),
                    "samples": page.evaluate("(ts) => ts.map(t => window.__lab.sample(t))", times),
                }
            page.close()
        browser.close()
    httpd.shutdown()
    if a.mode == "geometry":
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(json.dumps({"fps": a.fps, "variants": result}) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
