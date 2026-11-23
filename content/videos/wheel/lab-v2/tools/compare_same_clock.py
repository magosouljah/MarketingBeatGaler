"""Phase metrics for a lab render that runs on the reference clock (lab V2).

Compares the render against the reference with the same windows (reference
seconds). Inputs are derived measurements only (motion-field JSON +
Reference Analysis V1 analysis.json). The reference file used here is the
Instagram encode, which starts one frame after the documented original.

    python tools/compare_same_clock.py REF_MOTION REF_ANALYSIS LAB_MOTION LAB_ANALYSIS OUT.json
"""
import json
import sys

import numpy as np

PHASES = {"fan-out": (1.2, 1.6), "wheel": (1.6, 3.0), "approach": (3.0, 3.65), "riffle": (3.65, 4.35), "clear": (4.35, 6.0)}
KEYS = ["coverage", "speed_med", "affine_residual", "speed_cv", "coherence", "curl", "occlusion_proxy"]
REF_OFFSET = 1 / 30


def window(mf, a, b, off):
    rows = [r for r in mf["pairs"] if a - off <= r["time"] < b - off]
    return {k: (round(float(np.median([r[k] for r in rows if r.get(k) is not None])), 4)
                if any(r.get(k) is not None for r in rows) else None) for k in KEYS}


def energy(an, off):
    e = {p: float(np.mean([f["difference_mean"] for f in an["frames"]
                           if f["difference_mean"] is not None and a - off <= f["time_seconds"] < b - off]))
         for p, (a, b) in PHASES.items()}
    pk = max(e.values())
    return {p: round(v / pk, 3) for p, v in e.items()}


def main():
    rm, ra, lm, la, out = sys.argv[1:6]
    rm, ra, lm, la = (json.load(open(x)) for x in (rm, ra, lm, la))
    res = {"phases": PHASES, "reference": {"energy": energy(ra, REF_OFFSET), "motion": {p: window(rm, a, b, REF_OFFSET) for p, (a, b) in PHASES.items()}},
           "lab": {"energy": energy(la, 0), "motion": {p: window(lm, a, b, 0) for p, (a, b) in PHASES.items()}}}
    json.dump(res, open(out, "w"), indent=1)
    for who in ("reference", "lab"):
        print(who, "energy", res[who]["energy"])
        for p, m in res[who]["motion"].items():
            print("   ", p, {k: m[k] for k in ("coverage", "speed_med", "curl", "occlusion_proxy", "speed_cv")})


if __name__ == "__main__":
    main()
