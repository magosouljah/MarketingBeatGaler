"""Compare the three lab renders against the Apple Music reference by phase.

Inputs are derived measurements only (no reference pixels are read here):
- motion-field JSON (shared.motion_metrics.motion_field) for the reference
  and for each render;
- Reference Analysis V1 analysis.json (64x64 grayscale consecutive difference)
  for the reference and each render.

Phases are matched by ROLE, not by clock time: our 6 s blocking is an original
choreography with its own timing. Reference times are original-file seconds;
the local encode starts 0.1 s later (see apple-music-orbit-v1/PHASE2-RERUN.md).

    python tools/compare_reference.py REF_MOTION.json REF_ANALYSIS.json EVIDENCE_DIR OUT.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REF_OFFSET = 0.1  # local reference time = original time - 0.1 s
REF_PHASES = {"entrance": (1.2, 1.6), "orbit": (1.6, 3.0), "climax": (3.0, 4.35), "hold": (4.35, 6.0)}
LAB_PHASES = {"entrance": (0.0, 1.4), "orbit": (1.4, 3.3), "climax": (3.3, 4.9), "hold": (4.9, 6.0)}
KEYS = ["coverage", "speed_med", "affine_residual", "speed_cv", "coherence", "curl", "occlusion_proxy"]


def window(mf, t0, t1):
    rows = [r for r in mf["pairs"] if t0 <= r["time"] < t1]
    out = {}
    for k in KEYS:
        vals = [r[k] for r in rows if r.get(k) is not None]
        out[k] = round(float(np.median(vals)), 4) if vals else None
    return out


def energy(analysis, t0, t1):
    vals = [f["difference_mean"] for f in analysis["frames"]
            if f["difference_mean"] is not None and t0 <= f["time_seconds"] < t1]
    return round(float(np.mean(vals)), 4) if vals else None


def energy_shape(analysis, phases, offset=0.0):
    e = {p: energy(analysis, a - offset, b - offset) for p, (a, b) in phases.items()}
    peak = max(v for v in e.values() if v is not None)
    return {"mean_difference": e, "relative_to_peak": {p: round(v / peak, 3) if v else None for p, v in e.items()},
            "peak_phase": max(e, key=lambda p: e[p] or 0)}


def main():
    ref_mf = json.load(open(sys.argv[1]))
    ref_an = json.load(open(sys.argv[2]))
    ev = Path(sys.argv[3])
    out = {"note": "Phase-matched medians. Image metrics, not 3D truth. Reference phases in original seconds.",
           "reference_phases": REF_PHASES, "lab_phases": LAB_PHASES,
           "reference": {"motion": {p: window(ref_mf, a - REF_OFFSET, b - REF_OFFSET) for p, (a, b) in REF_PHASES.items()},
                         "energy": energy_shape(ref_an, REF_PHASES, REF_OFFSET)},
           "variants": {}}
    for v in "abc":
        mf = json.load(open(ev / f"motion-field-{v}.json"))
        an = json.load(open(ev / "reference-intelligence" / f"variant-{v}" / "analysis.json"))
        out["variants"][v] = {"motion": {p: window(mf, a, b) for p, (a, b) in LAB_PHASES.items()},
                              "energy": energy_shape(an, LAB_PHASES)}
    Path(sys.argv[4]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    for name, block in [("REF", out["reference"])] + [(k.upper(), b) for k, b in out["variants"].items()]:
        print(name, "energy", block["energy"]["relative_to_peak"], "peak:", block["energy"]["peak_phase"])
        for p, m in block["motion"].items():
            print("   ", p, m)


if __name__ == "__main__":
    main()
