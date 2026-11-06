"""Grid-search RIG overrides against the reference on three measures (LOCAL QA).

For each candidate and each time:
  iou      foreground-silhouette IoU (90x160), reference text box excluded
  orient   similarity of card-edge orientations: 8-bin gradient-orientation
           histograms of the silhouettes in a 3x4 grid of cells, cosine per
           cell, averaged. Catches cards leaning the wrong way, which IoU
           cannot see (owner, 2026-11-06: frame ~99 cards lean ~-45 deg, the
           reference 45-90 deg).
  backs    share of visible on-screen card area showing its BACK face, from
           the exact scene geometry (the reference never shows a back).
  axis     silhouette major-axis angle (second moments, y up); the score
           penalises |angle difference| / 90 deg. Owner frame ~99: the
           reference ring sits at 45-90 deg, ours at about -45 deg.
score = 0.45*iou + 0.55*orient - 1.0*backs - 0.5*axis_err

    FIT_REF_FRAMES=<ref frames dir> python tools/fit_pose.py GRID.json OUT.json --at 1.9,2.4,2.9,3.3
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
REF_GROUND = (243, 243, 243)
TEXT_ON = (1.6, 3.65)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def mask(img, ground, t):
    a = np.asarray(img.convert("RGB").resize((180, 320), Image.BILINEAR)).astype(float)
    m = np.linalg.norm(a - np.array(ground), axis=2) > 30
    if TEXT_ON[0] <= t < TEXT_ON[1]:
        m[118:152, 44:144] = False
    return m


def axis_angle(m):
    ys, xs = np.nonzero(m)
    if len(xs) < 50:
        return None
    x = xs - xs.mean()
    y = -(ys - ys.mean())
    cxx, cyy, cxy = (x * x).mean(), (y * y).mean(), (x * y).mean()
    return float(0.5 * np.degrees(np.arctan2(2 * cxy, cxx - cyy)))


def angle_err(a, b):
    if a is None or b is None:
        return 1.0
    d = (a - b + 90) % 180 - 90
    return abs(d) / 90


def orient_hist(m):
    f = m.astype(float)
    gy, gx = np.gradient(f)
    mag = np.hypot(gx, gy)
    ang = np.mod(np.arctan2(gy, gx), np.pi)  # edge orientation, 0..pi
    bins = np.minimum((ang / np.pi * 8).astype(int), 7)
    H, W = m.shape
    out = []
    for r in range(4):
        for c in range(3):
            sl = (slice(r * H // 4, (r + 1) * H // 4), slice(c * W // 3, (c + 1) * W // 3))
            out.append(np.bincount(bins[sl].ravel(), weights=mag[sl].ravel(), minlength=8))
    return np.array(out)


def orient_sim(a, b):
    sims, wts = [], []
    for ha, hb in zip(a, b):
        na, nb = np.linalg.norm(ha), np.linalg.norm(hb)
        if na < 1e-6 and nb < 1e-6:
            continue
        sims.append(float(ha @ hb / max(na * nb, 1e-9)))
        wts.append(na + nb)
    return float(np.average(sims, weights=wts)) if sims else 0.0


def back_share(sample):
    tot = back = 0.0
    for c in sample["cards"]:
        pts = c["corners"]
        if any(z >= 1 or z <= -1 for _, _, z, _ in pts):
            continue
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        if max(xs) < -1 or min(xs) > 1 or max(ys) < -1 or min(ys) > 1:
            continue
        area = 0.5 * abs(sum(xs[i] * ys[(i + 1) % 4] - xs[(i + 1) % 4] * ys[i] for i in range(4)))
        if not c.get("visible", True):
            continue
        tot += area
        if c["facing"] < -0.02 and c.get("backsRendered", True):
            back += area
    return back / tot if tot else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("grid", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--at", default="1.9,2.4,2.9,3.3")
    a = ap.parse_args()
    frames_dir = Path(os.environ["FIT_REF_FRAMES"])
    times = [float(x) for x in a.at.split(",")]
    refs = {}
    for t in times:
        m = mask(Image.open(frames_dir / f"{round(t * 30):06d}.png"), REF_GROUND, t)
        refs[t] = (m, orient_hist(m), axis_angle(m))
    grid = json.loads(a.grid.read_text())
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    res = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"),
                              args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
        page = b.new_page(viewport={"width": 720, "height": 1280})
        page.goto(f"http://127.0.0.1:{httpd.server_address[1]}/index.html")
        page.wait_for_function("window.__lab !== undefined", timeout=120000)
        page.add_style_tag(content=".word,#brand,#endcard{display:none!important}")
        ground = tuple(int(x) for x in page.evaluate(
            "getComputedStyle(document.getElementById('root')).backgroundColor").strip("rgb()").split(",")[:3])
        page.evaluate("async()=>{window.__m=await import('./src/wheel.js');}")
        for cand in grid:
            page.evaluate("""async (c)=>{const m=window.__m;const rig=Object.assign({},m.RIG,c);
              const cv=document.getElementById('stage');const f=cv.cloneNode();f.id='stage';cv.replaceWith(f);
              window.__x=m.createWheel(f,rig);await window.__x.ready;}""", cand)
            per = []
            for t in times:
                page.evaluate(f"window.__x.render({t})")
                om = mask(Image.open(io.BytesIO(page.screenshot())), ground, t)
                rm, rh, ra = refs[t]
                union = (om | rm).sum()
                iou = float((om & rm).sum() / union) if union else 0.0
                ori = orient_sim(orient_hist(om), rh)
                backs = back_share(page.evaluate(f"window.__x.sample({t})"))
                oa = axis_angle(om)
                per.append({"t": t, "iou": round(iou, 4), "orient": round(ori, 4), "backs": round(backs, 4),
                            "axis": None if oa is None else round(oa, 1), "ref_axis": None if ra is None else round(ra, 1),
                            "axis_err": round(angle_err(oa, ra), 4)})
            iou = np.mean([x["iou"] for x in per])
            ori = np.mean([x["orient"] for x in per])
            bk = np.mean([x["backs"] for x in per])
            ae = np.mean([x["axis_err"] for x in per])
            res.append({"score": round(float(0.45 * iou + 0.55 * ori - bk - 0.5 * ae), 4), "iou": round(float(iou), 4),
                        "orient": round(float(ori), 4), "backs": round(float(bk), 4), "axis_err": round(float(ae), 4),
                        "per": per, "cand": cand})
        b.close()
    httpd.shutdown()
    res.sort(key=lambda r: -r["score"])
    a.out.write_text(json.dumps(res, indent=1) + "\n")
    for r in res[:8]:
        c = {k: v for k, v in r["cand"].items() if k in ("label", "bladePitch", "rotation", "tip", "position", "scale", "pitch")}
        print(r["score"], "iou", r["iou"], "orient", r["orient"], "backs", r["backs"], "axis", [x["axis"] for x in r["per"]],
              "ref", [x["ref_axis"] for x in r["per"]], json.dumps(c)[:200])


if __name__ == "__main__":
    main()
