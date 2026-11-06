# Reference Analysis V1

Source: `wheel-v7.mp4`; SHA256 `52c08bd13ab44ce1a8afd3521ac8e7878f08ff4fc6afa8f8c5c8b27aa60698f8`.
Account: account-1. Full source-frame coverage: 180 frames.

## Direct measurements

Video: 720×1280; reported average FPS 30/1.
Presentation span: 5.966667 s (first to last frame, not container duration).
PTS are source presentation timestamps; local time subtracts the first video PTS.
Luma/difference values describe 64×64 grayscale thumbnails, not object velocities.

## Estimated temporal structure

No candidate exceeded the configured threshold; this does not prove a continuous shot.

## Audio stream timing

[]

## Human/agent annotations (not verified measurements)


## Estimated 2D trajectories

Normalized coded-image coordinates (x right, y down); velocities use actual PTS. No inferred Z or camera pose.

## Warnings

- 15 consecutive identical grayscale thumbnails; inspect holds/duplicates.

## Limitations / next checks

- Cut candidates are grayscale difference heuristics: flashes and fast motion can trigger them.
- No semantic object, text, material, illumination, camera or 3D reconstruction is automatic.
- Identical thumbnails may indicate a hold, compression or lost detail, not a duplicated source frame.
- Stream timing offsets are technical warnings, not proof of perceptual audiovisual desynchronization.
- No automatic artistic approval; annotations and candidate rules require evidence and review.

Review every constituent movement independently: translation, scale, visible rotation, overlap/occlusion, apparent depth and camera hypotheses.
Inspect timing/spacing, anticipation, arcs, overlapping action, typography, contrast, color, sound events and continuity on consecutive frames.
For reconstruction compare aligned local times and aspect ratios, then render a small original blocking test before shading.
