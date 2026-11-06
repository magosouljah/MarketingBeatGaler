"""Dense-motion field metrics for short motion-design clips.

Optional companion to ``shared.reference_analysis`` (which stays stdlib-only).
Requires ``numpy`` and ``opencv-python``. Every number here is a *2D image
measurement*: it describes how foreground pixels move on screen between two
consecutive decoded frames. None of them recovers 3D depth, camera pose or
easing curves; they are used to compare a reference against our own renders
with the same yardstick.

Per consecutive frame pair (t -> t+1), over moving foreground pixels:

- ``coverage``: fraction of the frame that differs from the estimated
  background colour.
- ``speed_med``: median flow magnitude, in frame heights per second.
- ``affine_residual``: RMS of the flow left after fitting ONE global 2D affine
  motion, divided by RMS flow. ~0 = the whole picture moves as one rigid
  plane (pan/zoom/rotation of a flat image). High = independent trajectories,
  perspective/parallax or depth-dependent motion.
- ``speed_cv``: coefficient of variation of flow magnitude (speed spread).
- ``coherence``: length of the mean unit flow vector (1 = everything moves in
  one direction, 0 = directions cancel, e.g. rotation or explosion).
- ``divergence``/``curl``: trace/antisymmetric part of the fitted affine
  matrix, per second (apparent expansion / in-plane rotation of the group).
- ``occlusion_proxy``: fraction of moving foreground pixels whose
  forward-backward flow disagrees (> 1 px + 5 %). Occlusion, disocclusion,
  entering/leaving frame and flow failure all raise it. A proxy, not a count.

Usage::

    python -m shared.motion_metrics.motion_field VIDEO OUT.json [--label NAME]
        [--start-frame N] [--end-frame M] [--height 640]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import cv2
import numpy as np

SCHEMA_VERSION = 1
MOVE_EPS_PX = 0.25
BG_DIST = 22.0
FARNEBACK = dict(pyr_scale=0.5, levels=5, winsize=21, iterations=4, poly_n=7,
                 poly_sigma=1.5, flags=0)


def read_frames(path: Path, height: int) -> tuple[list[np.ndarray], float]:
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise SystemExit(f"cannot open {path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frames = []
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        h, w = fr.shape[:2]
        if h != height:
            fr = cv2.resize(fr, (round(w * height / h), height), interpolation=cv2.INTER_AREA)
        frames.append(fr)
    cap.release()
    if len(frames) < 2:
        raise SystemExit("need at least two frames")
    return frames, float(fps)


def estimate_background(frames: list[np.ndarray]) -> np.ndarray:
    """Most frequent coarse colour across sampled frames (uniform-background clips)."""
    step = max(1, len(frames) // 24)
    px = np.concatenate([f[::8, ::8].reshape(-1, 3) for f in frames[::step]])
    q = (px // 8).astype(np.int32)
    keys = q[:, 0] * 1024 + q[:, 1] * 32 + q[:, 2]
    vals, counts = np.unique(keys, return_counts=True)
    k = vals[np.argmax(counts)]
    sel = px[keys == k]
    return sel.mean(axis=0)


def foreground(frame: np.ndarray, bg: np.ndarray) -> np.ndarray:
    d = np.linalg.norm(frame.astype(np.float32) - bg[None, None, :], axis=2)
    return d > BG_DIST


def pair_metrics(f0, f1, bg, fps):
    g0 = cv2.cvtColor(f0, cv2.COLOR_BGR2GRAY)
    g1 = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
    h, w = g0.shape
    fwd = cv2.calcOpticalFlowFarneback(g0, g1, None, **FARNEBACK)
    bwd = cv2.calcOpticalFlowFarneback(g1, g0, None, **FARNEBACK)
    fg = foreground(f0, bg) | foreground(f1, bg)
    coverage = float(foreground(f0, bg).mean())
    mag = np.linalg.norm(fwd, axis=2)
    mov = fg & (mag > MOVE_EPS_PX)
    out = {"coverage": round(coverage, 5), "moving_fraction": round(float(mov.mean()), 5)}
    n = int(mov.sum())
    if n < 200:
        out.update(dict(speed_med=0.0, affine_residual=None, speed_cv=None, coherence=None,
                        divergence=None, curl=None, occlusion_proxy=None, n=n))
        return out
    ys, xs = np.nonzero(mov)
    if n > 40000:
        idx = np.linspace(0, n - 1, 40000).astype(int)
        ys, xs = ys[idx], xs[idx]
    u = fwd[ys, xs, 0].astype(np.float64)
    v = fwd[ys, xs, 1].astype(np.float64)
    # normalised coordinates (frame height = 1) centred on the frame
    xn = (xs - w / 2) / h
    yn = (ys - h / 2) / h
    A = np.stack([xn, yn, np.ones_like(xn)], axis=1)
    cu, *_ = np.linalg.lstsq(A, u, rcond=None)
    cv_, *_ = np.linalg.lstsq(A, v, rcond=None)
    ru = u - A @ cu
    rv = v - A @ cv_
    rms_flow = math.sqrt(float(np.mean(u * u + v * v)))
    rms_res = math.sqrt(float(np.mean(ru * ru + rv * rv)))
    m = np.hypot(u, v)
    unit = np.stack([u, v], 1) / np.maximum(m[:, None], 1e-9)
    # forward-backward consistency
    bx = np.clip((xs + u).round().astype(int), 0, w - 1)
    by = np.clip((ys + v).round().astype(int), 0, h - 1)
    back = bwd[by, bx]
    fb = np.hypot(u + back[:, 0], v + back[:, 1])
    occ = fb > (1.0 + 0.05 * m)
    # affine matrix in px/frame per normalised unit -> per second, unitless rate
    a11, a12 = cu[0] / h, cu[1] / h
    a21, a22 = cv_[0] / h, cv_[1] / h
    out.update(dict(
        speed_med=round(float(np.median(m)) / h * fps, 5),
        affine_residual=round(rms_res / max(rms_flow, 1e-9), 5),
        speed_cv=round(float(m.std() / max(m.mean(), 1e-9)), 5),
        coherence=round(float(np.linalg.norm(unit.mean(axis=0))), 5),
        divergence=round(float((a11 + a22) * fps), 5),
        curl=round(float((a21 - a12) * fps), 5),
        occlusion_proxy=round(float(occ.mean()), 5),
        n=n,
    ))
    return out


def summarize(rows: list[dict], keys=("coverage", "speed_med", "affine_residual", "speed_cv",
                                      "coherence", "divergence", "curl", "occlusion_proxy")) -> dict:
    s = {}
    for k in keys:
        vals = [r[k] for r in rows if r.get(k) is not None]
        s[k] = round(float(np.median(vals)), 5) if vals else None
    sp = np.array([r["speed_med"] for r in rows], dtype=float)
    if len(sp) >= 3 and sp.mean() > 0:
        jerk = np.abs(np.diff(sp, 2))
        s["speed_jerk_ratio"] = round(float(np.median(jerk) / max(np.median(sp[sp > 0]) if (sp > 0).any() else 1, 1e-9)), 5)
        s["speed_p95_jump"] = round(float(np.percentile(np.abs(np.diff(sp)), 95)), 5)
    s["pairs"] = len(rows)
    return s


def analyze(frames, fps, start=0, end=None, label=None, source=None):
    end = len(frames) - 1 if end is None else min(end, len(frames) - 1)
    bg = estimate_background(frames)
    rows = []
    for i in range(start, end):
        r = pair_metrics(frames[i], frames[i + 1], bg, fps)
        r["frame"] = i
        r["time"] = round(i / fps, 5)
        rows.append(r)
    return {
        "schema_version": SCHEMA_VERSION,
        "label": label,
        "source": source,
        "fps": fps,
        "frame_height_px": frames[0].shape[0],
        "background_bgr": [round(float(c), 1) for c in bg],
        "range": [start, end],
        "method": "OpenCV Farneback dense flow t->t+1 and t+1->t; global 2D affine least squares on moving foreground pixels",
        "params": {"move_eps_px": MOVE_EPS_PX, "bg_dist": BG_DIST, "farneback": FARNEBACK},
        "opencv": cv2.__version__,
        "limitations": [
            "2D screen-space measurement only; no depth, camera pose or easing curve is recovered.",
            "Background estimate assumes a near-uniform backdrop; static text counts as foreground but rarely moves.",
            "Occlusion proxy also fires for frame entry/exit, motion blur and flow failure on large displacements.",
        ],
        "summary": summarize(rows),
        "pairs": rows,
    }


def window_summary(result: dict, t0: float, t1: float) -> dict:
    rows = [r for r in result["pairs"] if t0 <= r["time"] < t1]
    return summarize(rows) if rows else {"pairs": 0}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("video", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--label")
    ap.add_argument("--start-frame", type=int, default=0)
    ap.add_argument("--end-frame", type=int)
    ap.add_argument("--height", type=int, default=640)
    a = ap.parse_args(argv)
    if a.out.exists():
        raise SystemExit(f"refusing to overwrite {a.out}")
    data = a.video.read_bytes()
    frames, fps = read_frames(a.video, a.height)
    res = analyze(frames, fps, a.start_frame, a.end_frame, a.label,
                  {"name": a.video.name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                   "frames": len(frames)})
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["summary"]))


if __name__ == "__main__":
    sys.exit(main())
