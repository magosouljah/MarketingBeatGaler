# Reference Analysis V1

Source: `source.mkv`; SHA256 `5a4e21c0598ea6af03ff41820823956879bd915902c017df12b3aa64049bbfc5`.
Account: account-1. Full source-frame coverage: 60 frames.

## Direct measurements

Video: 160×96; reported average FPS 30/1.
Presentation span: 1.967000 s (first to last frame, not container duration).
PTS are source presentation timestamps; local time subtracts the first video PTS.
Luma/difference values describe 64×64 grayscale thumbnails, not object velocities.

## Estimated temporal structure

- Candidate cut at frame 30 / 1.000000 s; validate visually.

## Audio stream timing

[{"stream_index": 1, "start_pts_seconds": 0.0, "offset_from_video_seconds": 0.0, "sample_rate": "48000"}]

## Human/agent annotations (not verified measurements)


## Estimated 2D trajectories

Normalized coded-image coordinates (x right, y down); velocities use actual PTS. No inferred Z or camera pose.
- square-center: 3 annotated samples; evidence: Synthetic generator truth; coordinates in coded 160x96 image.; uncertainty: Generator truth supplied for demonstration; real reference needs manual tracking error bounds..

## Warnings

- 29 consecutive identical grayscale thumbnails; inspect holds/duplicates.

## Limitations / next checks

- Cut candidates are grayscale difference heuristics: flashes and fast motion can trigger them.
- No semantic object, text, material, illumination, camera or 3D reconstruction is automatic.
- Identical thumbnails may indicate a hold, compression or lost detail, not a duplicated source frame.
- Stream timing offsets are technical warnings, not proof of perceptual audiovisual desynchronization.
- No automatic artistic approval; annotations and candidate rules require evidence and review.

Review every constituent movement independently: translation, scale, visible rotation, overlap/occlusion, apparent depth and camera hypotheses.
Inspect timing/spacing, anticipation, arcs, overlapping action, typography, contrast, color, sound events and continuity on consecutive frames.
For reconstruction compare aligned local times and aspect ratios, then render a small original blocking test before shading.
