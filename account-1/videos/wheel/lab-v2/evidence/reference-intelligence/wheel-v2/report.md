# Reference Analysis V1

Source: `wheel-v2.mp4`; SHA256 `cdbb394a5c894c594a062af0545a96a18b5296b166ff52296e70da79cde90263`.
Account: account-1. Full source-frame coverage: 180 frames.

## Direct measurements

Video: 720×1280; reported average FPS 30/1.
Presentation span: 5.966667 s (first to last frame, not container duration).
PTS are source presentation timestamps; local time subtracts the first video PTS.
Luma/difference values describe 64×64 grayscale thumbnails, not object velocities.

## Estimated temporal structure

- Candidate cut at frame 115 / 3.833333 s; validate visually.
- Candidate cut at frame 116 / 3.866667 s; validate visually.
- Candidate cut at frame 121 / 4.033333 s; validate visually.
- Candidate cut at frame 122 / 4.066667 s; validate visually.
- Candidate cut at frame 123 / 4.100000 s; validate visually.
- Candidate cut at frame 124 / 4.133333 s; validate visually.
- Candidate cut at frame 125 / 4.166667 s; validate visually.

## Audio stream timing

[]

## Human/agent annotations (not verified measurements)


## Estimated 2D trajectories

Normalized coded-image coordinates (x right, y down); velocities use actual PTS. No inferred Z or camera pose.

## Warnings

- 56 consecutive identical grayscale thumbnails; inspect holds/duplicates.

## Limitations / next checks

- Cut candidates are grayscale difference heuristics: flashes and fast motion can trigger them.
- No semantic object, text, material, illumination, camera or 3D reconstruction is automatic.
- Identical thumbnails may indicate a hold, compression or lost detail, not a duplicated source frame.
- Stream timing offsets are technical warnings, not proof of perceptual audiovisual desynchronization.
- No automatic artistic approval; annotations and candidate rules require evidence and review.

Review every constituent movement independently: translation, scale, visible rotation, overlap/occlusion, apparent depth and camera hypotheses.
Inspect timing/spacing, anticipation, arcs, overlapping action, typography, contrast, color, sound events and continuity on consecutive frames.
For reconstruction compare aligned local times and aspect ratios, then render a small original blocking test before shading.
