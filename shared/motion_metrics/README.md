# Motion metrics (optional companion to Reference Analysis V1)

`shared/reference_analysis` stays stdlib-only. This package adds two **optional** measurements that need `numpy` and `opencv-python(-headless)`. Both describe 2D screen motion only: no depth, camera pose or easing curve is recovered.

```bash
pip install numpy opencv-python-headless
python -m shared.motion_metrics.motion_field VIDEO OUT.json [--label NAME]
python -m shared.motion_metrics.klt_track VIDEO SEEDS.json TRACKS.json      # output is a valid --tracks file for the V1 pipeline
python -m unittest discover -s shared/motion_metrics/tests -t . -v
```

## `motion_field`

OpenCV Farneback flow forward and backward for every consecutive frame pair, over pixels that differ from the estimated uniform background and move > 0.25 px. Per pair and summarised:

| Field | Meaning |
| --- | --- |
| `coverage` | fraction of the frame that is foreground (density / negative space) |
| `speed_med` | median flow magnitude, frame heights per second |
| `affine_residual` | flow RMS left after one global 2D affine fit ÷ flow RMS. **Does not separate a rigid 3D orbit from independent motion** (a rigid helix rotating about a vertical axis scores ~0.8). Use it to compare image structure, not to prove rigidity |
| `speed_cv` | spread of speeds (uniform carousel → low) |
| `coherence` | length of the mean unit flow vector (1 = everything moves one way) |
| `divergence`, `curl` | expansion and in-plane rotation rates of the affine fit, per second |
| `occlusion_proxy` | share of moving pixels failing the forward-backward check: occlusion, entry/exit and flow failure all raise it |

Large displacements (> ~100 px/frame at 720×1280) exceed the flow's range and are underestimated; check `klt_track` failures and look at the frames.

## `klt_track`

Authored ROI seeds → `goodFeaturesToTrack` → pyramidal Lucas–Kanade with a forward-backward check. The point is the median of surviving features (a cluster estimate, not a card centre). A track stops at identity loss instead of bridging it. Per-seed `fb_max_px` and `min_survival` are recorded in the evidence string.

First use: [Apple Music Phase 2 rerun](../../account-1/research/reference-analysis/apple-music-orbit-v1/PHASE2-RERUN.md) and [Choreography Lab V1](../../account-1/creative-assets/choreography-lab-v1/RESULTS.md).
