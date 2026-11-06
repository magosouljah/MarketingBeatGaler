"""Side-by-side stills: reference vs. the lab V2 wheel at the same reference times.

LOCAL QA ONLY: the reference is third-party footage; never commit the output.
Reads the lab through a static server in headless Chrome (window.__lab.render(t)),
the reference through FFmpeg. Text layers are hidden by default so the sheet
compares cover structure; pass --with-type to keep them.

    python tools/compare_frames.py REF.mp4 OUT.jpg --at 1.3,1.5,1.9,2.5,3.0,3.4,3.7,3.9,4.1,4.3 [--ref-offset 0.0333]
--ref-offset: seconds to subtract from reference time to reach the file's own
clock (the Instagram encode starts one frame after the documented original).
"""
from __future__ import annotations

import argparse
import functools
import http.server
import io
import os
import subprocess
import threading
from pathlib import Path

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1] / "hyperframes"


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def ref_frame(path, t):
    out = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(t, 0):.4f}", "-i", str(path), "-frames:v", "1",
                          "-f", "image2pipe", "-vcodec", "png", "-"], check=True, capture_output=True).stdout
    return Image.open(io.BytesIO(out)).convert("RGB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ref", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--at", default="1.3,1.5,1.9,2.5,3.0,3.4,3.7,3.9,4.1,4.3")
    ap.add_argument("--ref-offset", type=float, default=1 / 30)
    ap.add_argument("--width", type=int, default=180)
    ap.add_argument("--with-type", action="store_true")
    a = ap.parse_args()
    times = [float(x) for x in a.at.split(",")]
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    ours = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"),
                              args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
        page = b.new_page(viewport={"width": 720, "height": 1280})
        page.goto(f"http://127.0.0.1:{httpd.server_address[1]}/index.html")
        page.wait_for_function("window.__lab !== undefined", timeout=120000)
        if not a.with_type:
            page.add_style_tag(content=".word,#brand,#endcard{display:none!important}")
        for t in times:
            page.evaluate(f"window.__lab.render({t})")
            ours.append(Image.open(io.BytesIO(page.screenshot())).convert("RGB"))
        b.close()
    httpd.shutdown()
    w = a.width
    h = int(w * 16 / 9)
    sheet = Image.new("RGB", (len(times) * (w + 4), 2 * (h + 16)), "white")
    d = ImageDraw.Draw(sheet)
    for i, t in enumerate(times):
        x = i * (w + 4)
        sheet.paste(ref_frame(a.ref, t - a.ref_offset).resize((w, h)), (x, 16))
        sheet.paste(ours[i].resize((w, h)), (x, h + 32))
        d.text((x + 3, 2), f"REF t={t:.2f}", fill="black")
        d.text((x + 3, h + 18), f"LAB t={t:.2f}", fill="black")
    sheet.save(a.out, quality=85)


if __name__ == "__main__":
    main()
