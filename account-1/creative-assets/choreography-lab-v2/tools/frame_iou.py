"""Frame-by-frame silhouette agreement with the reference (LOCAL QA).

For every reference frame in a time range, renders the lab at the same time
(text layers hidden), builds a foreground mask for both (pixels that differ
from each film's own ground colour; the reference text box is excluded while
its words are on screen) and reports IoU per frame and per phase. It measures
where the covers are on screen, not their art, orientation or depth: read it
together with the side-by-side frames.

    python tools/frame_iou.py REF_FRAMES_DIR OUT.json [--start 1.23] [--end 4.4] [--label v4]
REF_FRAMES_DIR: Reference Analysis V1 frames of the Instagram encode (file
frame N = original frame N, 30 fps clock).
"""
from __future__ import annotations

import argparse
import functools
import http.server
import io
import json
import os
import threading
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1] / "hyperframes"
PHASES = {"appear": (1.2, 1.6), "wheel": (1.6, 3.0), "approach": (3.0, 3.65), "riffle": (3.65, 4.35)}
REF_GROUND = (243, 243, 243)
TEXT_ON = (1.6, 3.65)  # reference words inside the ring


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def mask(img, ground, t=None):
    a = np.asarray(img.convert("RGB").resize((90, 160), Image.BILINEAR)).astype(float)
    m = np.linalg.norm(a - np.array(ground), axis=2) > 30
    if t is not None and TEXT_ON[0] <= t < TEXT_ON[1]:
        m[59:76, 22:72] = False
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("frames", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--start", type=float, default=1.23)
    ap.add_argument("--end", type=float, default=4.4)
    ap.add_argument("--label", default="lab")
    a = ap.parse_args()
    frames = list(range(round(a.start * 30), round(a.end * 30) + 1))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    rows = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"),
                              args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
        page = b.new_page(viewport={"width": 720, "height": 1280})
        page.goto(f"http://127.0.0.1:{httpd.server_address[1]}/index.html")
        page.wait_for_function("window.__lab !== undefined", timeout=120000)
        page.add_style_tag(content=".word,#brand,#endcard{display:none!important}")
        ground = tuple(int(x) for x in page.evaluate(
            "getComputedStyle(document.getElementById('root')).backgroundColor").strip("rgb()").split(",")[:3])
        for f in frames:
            t = f / 30
            page.evaluate(f"window.__lab.render({t})")
            ours = mask(Image.open(io.BytesIO(page.screenshot())), ground)
            ref = mask(Image.open(a.frames / f"{f:06d}.png"), REF_GROUND, t)
            ours_t = ours.copy()
            if TEXT_ON[0] <= t < TEXT_ON[1]:
                ours_t[59:76, 22:72] = False
            union = (ours_t | ref).sum()
            rows.append({"frame": f, "t": round(t, 4), "iou": round(float((ours_t & ref).sum() / union), 4) if union else None,
                         "ours_cover": round(float(ours_t.mean()), 4), "ref_cover": round(float(ref.mean()), 4)})
        b.close()
    httpd.shutdown()
    phases = {}
    for name, (t0, t1) in PHASES.items():
        v = [r["iou"] for r in rows if t0 <= r["t"] < t1 and r["iou"] is not None]
        phases[name] = round(float(np.mean(v)), 4) if v else None
    allv = [r["iou"] for r in rows if r["iou"] is not None]
    out = {"label": a.label, "method": "foreground-mask IoU per frame at 90x160; text box excluded 1.6-3.65 s",
           "phases": phases, "mean": round(float(np.mean(allv)), 4), "frames": rows}
    a.out.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(a.label, "mean", out["mean"], phases)


if __name__ == "__main__":
    main()
