"""Ground-truth choreography metrics from the lab's exact scene geometry.

Input: JSON from `lab_capture.py geometry` (projected corners of every card,
camera position, card facing, per frame). These numbers come from the source
code, not from pixels, so they verify what each variant actually does.

Per frame (visible = card centre in front of the camera and its quad
intersects the frame):
  visible            number of visible cards
  scale_contrast     p90/p10 of sqrt(on-screen area): near/far size contrast
  overlap_pairs      pairs of visible quads whose on-screen polygons intersect
  occluded_share     sum of pairwise overlap area / sum of visible area
  edge_on_share      visible cards with |facing| < 0.25 (seen almost edge-on)
  speed_cv           coefficient of variation of on-screen centroid speeds
  coherence          |mean unit velocity| (1 = all move one way)
  max_accel          largest centroid second difference (px/frame^2)
Per variant:
  rigid3d_residual   RMS residual of the best single 3D rigid motion (Kabsch)
                     between consecutive frames, world units/frame
  camera_path        camera travel (world units) and peak camera acceleration
  min_cam_dist       closest any card centre comes to the lens

    python tools/geometry_metrics.py GEOMETRY.json OUT.json
"""
from __future__ import annotations

import json
import sys

import cv2
import numpy as np

W, H = 720, 1280
WINDOWS = [("entrance", 0.0, 1.4), ("orbit", 1.4, 3.3), ("peel-gather", 3.3, 4.9), ("land-hold", 4.9, 6.0)]
FRAME = np.array([[0, 0], [W, 0], [W, H], [0, H]], np.float32)


def to_px(c):
    return np.array([[(x + 1) / 2 * W, (1 - y) / 2 * H] for x, y, *_ in c], np.float32)


def poly_area(p):
    return float(abs(cv2.contourArea(p)))


def inter_area(p, q):
    a, _ = cv2.intersectConvexConvex(p, q)
    return float(a)


def ordered(p):
    # quads from the scene are planar and convex; enforce consistent winding
    return p if cv2.contourArea(p, oriented=True) >= 0 else p[::-1].copy()


def kabsch_residual(P, Q):
    pc, qc = P.mean(0), Q.mean(0)
    X, Y = P - pc, Q - qc
    U, _, Vt = np.linalg.svd(X.T @ Y)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1, 1, d])
    R = Vt.T @ D @ U.T
    res = (R @ X.T).T - Y
    return float(np.sqrt((res ** 2).sum(1).mean()))


def frame_metrics(sample, prev_cent, prev2_cent):
    vis, areas, polys, facing, cents = [], [], [], [], {}
    for c in sample["cards"]:
        corners = c["corners"]
        if any(z >= 1 or z <= -1 for _, _, z, _ in corners):
            continue  # behind the lens or beyond clip planes
        p = ordered(to_px(corners))
        on = inter_area(p, FRAME)
        if on <= 1:
            continue
        vis.append(c["id"])
        areas.append(on)
        polys.append(p)
        facing.append(abs(c["facing"]))
        cents[c["id"]] = p.mean(0)
    n = len(vis)
    out = {"t": sample["t"], "visible": n}
    if n == 0:
        return out, cents
    s = np.sqrt(np.array(areas))
    out["scale_contrast"] = float(np.percentile(s, 90) / max(np.percentile(s, 10), 1e-6)) if n >= 3 else None
    pairs, ov = 0, 0.0
    for i in range(n):
        for j in range(i + 1, n):
            a = inter_area(polys[i], polys[j])
            if a > 25:
                pairs += 1
                ov += a
    out["overlap_pairs"] = pairs
    out["occluded_share"] = ov / max(sum(areas), 1e-6)
    out["edge_on_share"] = float(np.mean(np.array(facing) < 0.25))
    vel, acc = [], []
    for k, cpos in cents.items():
        if k in prev_cent:
            vel.append(cpos - prev_cent[k])
            if k in prev2_cent:
                acc.append(np.linalg.norm(cpos - 2 * prev_cent[k] + prev2_cent[k]))
    if len(vel) >= 3:
        v = np.array(vel)
        sp = np.linalg.norm(v, axis=1)
        out["speed_px_s_med"] = float(np.median(sp) * 30)
        out["speed_cv"] = float(sp.std() / max(sp.mean(), 1e-6))
        moving = sp > 0.2
        if moving.sum() >= 3:
            u = v[moving] / sp[moving, None]
            out["coherence"] = float(np.linalg.norm(u.mean(0)))
    if acc:
        out["max_accel"] = float(max(acc))
    return out, cents


def summarize(rows, t0, t1):
    sel = [r for r in rows if t0 <= r["t"] < t1]
    keys = ["visible", "scale_contrast", "overlap_pairs", "occluded_share", "edge_on_share",
            "speed_px_s_med", "speed_cv", "coherence", "max_accel"]
    out = {}
    for k in keys:
        vals = [r[k] for r in sel if r.get(k) is not None]
        if not vals:
            out[k] = None
        elif k == "max_accel":
            out[k] = round(float(np.max(vals)), 3)
        else:
            out[k] = round(float(np.median(vals)), 4)
    return out


def variant_metrics(v):
    samples = v["samples"]
    rows, prev, prev2 = [], {}, {}
    for s in samples:
        r, cents = frame_metrics(s, prev, prev2)
        rows.append(r)
        prev2, prev = prev, cents
    rigid = []
    for a, b in zip(samples, samples[1:]):
        P = np.array([c["world"] for c in a["cards"]])
        Q = np.array([c["world"] for c in b["cards"]])
        rigid.append(kabsch_residual(P, Q))
    cam = np.array([s["camera"] for s in samples])
    steps = np.linalg.norm(np.diff(cam, axis=0), axis=1)
    cam_acc = np.linalg.norm(np.diff(cam, 2, axis=0), axis=1) if len(cam) > 2 else np.zeros(1)
    min_dist = min(c["camDist"] for s in samples for c in s["cards"])
    accel_all = [r["max_accel"] for r in rows if r.get("max_accel") is not None]
    return {
        "label": v["label"],
        "windows": {name: summarize(rows, a, b) for name, a, b in WINDOWS},
        "whole": summarize(rows, 0, 99),
        "rigid3d_residual_med": round(float(np.median(rigid)), 5),
        "rigid3d_residual_max": round(float(np.max(rigid)), 5),
        "camera_travel": round(float(steps.sum()), 4),
        "camera_peak_accel": round(float(cam_acc.max()), 5),
        "min_cam_dist": round(float(min_dist), 3),
        "max_centroid_accel_px": round(float(max(accel_all)), 2) if accel_all else None,
        "frames": rows,
    }


def main():
    src, dst = sys.argv[1], sys.argv[2]
    g = json.load(open(src, encoding="utf-8"))
    out = {"source": "lab_capture.py geometry (exact scene state)", "fps": g["fps"], "windows": WINDOWS,
           "variants": {k: variant_metrics(v) for k, v in g["variants"].items()}}
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    for k, v in out["variants"].items():
        print(k, {x: v[x] for x in ["rigid3d_residual_med", "camera_travel", "camera_peak_accel", "min_cam_dist", "max_centroid_accel_px"]})
        for w, s in v["windows"].items():
            print("   ", w, s)


if __name__ == "__main__":
    main()
