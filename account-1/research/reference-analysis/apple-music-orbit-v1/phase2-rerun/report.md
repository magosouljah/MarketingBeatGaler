# Reference Analysis V1

Source: `source.mp4`; SHA256 `885dc1c1c3dd641670405ba637aff5865cc7fd44cbe713614038fa4cebe64c14`.
Account: account-1. Full source-frame coverage: 178 frames.

## Direct measurements

Video: 720×1280; reported average FPS 30/1.
Presentation span: 5.900000 s (first to last frame, not container duration).
PTS are source presentation timestamps; local time subtracts the first video PTS.
Luma/difference values describe 64×64 grayscale thumbnails, not object velocities.

## Estimated temporal structure

No candidate exceeded the configured threshold; this does not prove a continuous shot.

## Audio stream timing

[{"stream_index": 1, "start_pts_seconds": 0.0, "offset_from_video_seconds": 0.0, "sample_rate": "44100"}]

## Human/agent annotations (not verified measurements)

- [estimate] This 720x1280 file is a different encode of the documented Apple Music original, missing the first 3 frames (0.1 s): local frame i = original frame i+3. (frames 0–177). Evidence: Per-interval means of the 64x64 grayscale consecutive difference match MEASUREMENTS.json best at offset -3 (SSE 0.000148 vs 0.000333/0.000372 at -4/-2); top three difference peaks at local 119/124/113 = original 122/127/116, exactly the documented peaks.. Method: Offset search over -8..8 frames against the 8 documented interval means; peak comparison.. Uncertainty: Not byte-identical (SHA256 885dc1c1... vs 74301c7f...); resolution, encoder and trailing frames differ; visual content may still differ in ways the thumbnail metric cannot see..
- [observation] Covers appear as a compact, steeply tilted cluster right of centre and unfold into an open arc within ~0.4 s; no stable ring exists yet. (frames 33–45). Evidence: Local frames 33-45 (original 1.20-1.60 s), contact sheets at every 3rd frame.. Method: Visual inspection of consecutive decoded frames.. Uncertainty: Whether the unfold is camera, group rotation or per-card motion is not observable..
- [observation] A wreath of covers circles a stable typographic centre; left-side covers are near edge-on slivers while right/lower-right covers show nearly full faces and larger apparent size. (frames 45–87). Evidence: Local frames 45-87 (original 1.6-3.0 s); grid inspection of local frame 60.. Method: Visual inspection with a 10x10 normalised grid.. Uncertainty: Consistent with radially oriented cards on a tilted ring seen off-axis, but not uniquely..
- [interpretation] The wreath reads as a strong rotation (curl ~5.8/s) yet ~43 % of flow RMS is not explained by one 2D affine motion, so covers do more than ride one rigid flat ring. (frames 45–87). Evidence: reference motion-field-v1.json window 1.5-2.9 s local: curl 5.76, affine_residual 0.43, coherence 0.14, speed_cv 0.41.. Method: Farneback dense flow + global affine least squares on moving foreground (shared.motion_metrics).. Uncertainty: Perspective of a rigid 3D ring also produces non-affine residual; the rigid-orbit control render is the discriminating test..
- [observation] The wreath expands past the frame; top covers stream outward as thin slivers while lower-right covers grow large and frontal, handing off into a foreground stack. (frames 87–106). Evidence: Local frames 87-106 (original 3.0-3.63 s); motion-field window: speed 0.94 H/s, affine_residual 0.78, occlusion proxy 0.59.. Method: Visual inspection plus dense-flow metrics.. Uncertainty: Camera dolly versus ring scale-up cannot be separated monocularly..
- [observation] Foreground: three to four large covers lie back in steep perspective in a staggered diagonal stack; consecutive frames show DIFFERENT covers at nearly the same layout positions, roughly one cover change per frame. (frames 106–126). Evidence: Local frames 100-123 inspected one by one; e.g. rose/blue/orange/red/forest covers occupy the top slot on local 110/111/112/113/114. Seeded KLT on local 106 lost all features in one step (median displacement 112-170 px/frame, forward-backward error 45-400 px).. Method: Frame-by-frame inspection; pyramidal LK diagnostic.. Uncertainty: Dense-flow speed in this window is underestimated because displacement exceeds flow capacity..
- [hypothesis] The riffle is either (H1) a conveyor moving about one slot spacing per frame, which strobes at 30 fps, or (H2) an authored per-frame cover swap on near-static slots. (frames 106–126). Evidence: Absence of visible motion blur and stable slot layout across local 110-121; slot drift is upward and small.. Method: Competing explanations; discriminating test: render both at 60 fps and compare 30 fps decimation against the reference look.. Uncertainty: Both produce the same 30 fps frames; not resolvable from this file..
- [observation] After the last covers exit upward, a static typographic end card holds for ~1.5 s. (frames 131–177). Evidence: Local frames 131-177, difference_mean below 0.002.. Method: Measured thumbnail difference plus inspection.. Uncertainty: Out of scope for this experiment; not reproduced..

## Estimated 2D trajectories

Normalized coded-image coordinates (x right, y down); velocities use actual PTS. No inferred Z or camera pose.
- wreath-orange-card: 5 annotated samples; evidence: Authored ROI [0.56, 0.45, 0.66, 0.6] on coded frame 60; OpenCV 5.0.0 goodFeaturesToTrack (35 seeds) + pyramidal LK with forward-backward check; fb<1.0px, min survival 0.4; median of survivors; 18 survive at frame 64. Orange/red cover in lower-right arc of the wreath.; uncertainty: Feature-cluster median, not a verified card centre; perspective, overlap and partial exit bias it; stopped at identity-loss threshold..
- wreath-pink-large-card: 8 annotated samples; evidence: Authored ROI [0.76, 0.37, 0.95, 0.52] on coded frame 60; OpenCV 5.0.0 goodFeaturesToTrack (104 seeds) + pyramidal LK with forward-backward check; fb<1.0px, min survival 0.4; median of survivors; 43 survive at frame 67. Large pink cover on right side of the wreath.; uncertainty: Feature-cluster median, not a verified card centre; perspective, overlap and partial exit bias it; stopped at identity-loss threshold..

## Warnings


## Limitations / next checks

- Cut candidates are grayscale difference heuristics: flashes and fast motion can trigger them.
- No semantic object, text, material, illumination, camera or 3D reconstruction is automatic.
- Identical thumbnails may indicate a hold, compression or lost detail, not a duplicated source frame.
- Stream timing offsets are technical warnings, not proof of perceptual audiovisual desynchronization.
- No automatic artistic approval; annotations and candidate rules require evidence and review.

Review every constituent movement independently: translation, scale, visible rotation, overlap/occlusion, apparent depth and camera hypotheses.
Inspect timing/spacing, anticipation, arcs, overlapping action, typography, contrast, color, sound events and continuity on consecutive frames.
For reconstruction compare aligned local times and aspect ratios, then render a small original blocking test before shading.
