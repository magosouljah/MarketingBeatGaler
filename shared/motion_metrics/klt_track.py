"""Seeded sparse KLT tracks -> Reference Analysis V1 ``--tracks`` JSON.

Seeds are authored ROIs (normalised x0,y0,x1,y1 on one frame). The reported
point is the median of surviving feature points: an estimate of a feature
cluster centre, NOT a verified card centre. A track stops when fewer than
``min_survival`` of the seed features remain or the forward-backward error
check rejects them, so identity loss is not bridged.

    python -m shared.motion_metrics.klt_track VIDEO SEEDS.json OUT.json
SEEDS.json: [{"id", "frame", "roi": [x0,y0,x1,y1], "end_frame", "note", "fb_max_px"?, "min_survival"?}]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import cv2
import numpy as np

LK = dict(winSize=(25, 25), maxLevel=4,
          criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.01))


def load_gray(path):
    cap = cv2.VideoCapture(str(path))
    out = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        out.append(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY))
    return out


def track(frames, seed, min_survival=0.4, step=1):
    fb_max = float(seed.get("fb_max_px", 1.0))
    min_survival = float(seed.get("min_survival", min_survival))
    g = frames[seed["frame"]]
    h, w = g.shape
    x0, y0, x1, y1 = seed["roi"]
    mask = np.zeros_like(g)
    mask[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)] = 255
    p = cv2.goodFeaturesToTrack(g, 120, 0.01, 4, mask=mask)
    if p is None:
        return [], 0
    n0 = len(p)
    samples = []
    prev = g
    fi = seed["frame"]
    end = min(seed["end_frame"], len(frames) - 1)
    while True:
        med = np.median(p.reshape(-1, 2), axis=0)
        samples.append({"frame": fi, "x": round(float(med[0] / w), 4), "y": round(float(med[1] / h), 4),
                        "survivors": int(len(p))})
        if fi + step > end:
            break
        nxt = frames[fi + step]
        p1, st, _ = cv2.calcOpticalFlowPyrLK(prev, nxt, p, None, **LK)
        p0r, st2, _ = cv2.calcOpticalFlowPyrLK(nxt, prev, p1, None, **LK)
        fb = np.linalg.norm((p - p0r).reshape(-1, 2), axis=1)
        good = (st.ravel() == 1) & (st2.ravel() == 1) & (fb < fb_max)
        p = p1[good].reshape(-1, 1, 2)
        fi += step
        prev = nxt
        if len(p) < max(8, min_survival * n0):
            break
    return samples, n0


def main(argv=None):
    argv = argv or sys.argv[1:]
    video, seeds_path, out = Path(argv[0]), Path(argv[1]), Path(argv[2])
    if out.exists():
        raise SystemExit(f"refusing to overwrite {out}")
    frames = load_gray(video)
    seeds = json.loads(seeds_path.read_text(encoding="utf-8"))
    tracks = []
    for s in seeds:
        samples, n0 = track(frames, s)
        if len(samples) < 2:
            continue
        last = samples[-1]
        tracks.append({
            "id": s["id"],
            "evidence": (f"Authored ROI {s['roi']} on coded frame {s['frame']}; OpenCV {cv2.__version__} "
                         f"goodFeaturesToTrack ({n0} seeds) + pyramidal LK with forward-backward check; "
                         f"fb<{s.get('fb_max_px', 1.0)}px, min survival {s.get('min_survival', 0.4)}; median of survivors; {last['survivors']} survive at frame {last['frame']}. {s.get('note', '')}").strip(),
            "uncertainty": "Feature-cluster median, not a verified card centre; perspective, overlap and partial exit bias it; stopped at identity-loss threshold.",
            "samples": [{"frame": x["frame"], "x": x["x"], "y": x["y"]} for x in samples],
        })
    out.write_text(json.dumps(tracks, indent=1) + "\n", encoding="utf-8")
    for t in tracks:
        a, b = t["samples"][0], t["samples"][-1]
        print(t["id"], len(t["samples"]), a, b)


if __name__ == "__main__":
    main()
