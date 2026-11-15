# BeatGaler — First Video / Cover Orbit 3D — iteration 01

**Status: experimental; NOT creatively approved.** This creates the *orbit only*, not the full advertisement, narration, file morph, landing reveal or UI demonstration. The original approved script is unchanged.

## Source and preview

- `index.html`: stand-alone 720 × 1280, 5.8 s, 24 fps video composition. Open via a static server (for instance `python -m http.server 4173` in this folder), not `file://`. WebGL2 is the primary 3D renderer. A limited Canvas2D visual fallback is provided for GPU-restricted browsers; the fallback **does not establish WebGL visual quality**.
- `assets/covers/`: 24 **exact copies** of the optimized user-supplied cover files from BeatGaler repository branch `design/beatgaler-design-system-lab-v1`, `DESIGN/shared/assets/real-covers/`, verified by identical Git blob SHA. The originals are real BeatGaler Design Lab assets, **not cleared for public marketing or redistribution**. Seek explicit asset permissions before publishing ads.
- `tools/preview_capture.py`: deterministic local browser capture via Playwright, FFmpeg; useful for checking framing, timing and making an H.264 preview. Requires `pip install playwright pillow`, `python -m playwright install chromium`, `ffmpeg`. It generates frames at exact `seekTo(t)` timestamps, not unreliable real-time screen recording. Run from this directory: `python tools/preview_capture.py --shots --frames 144 --fps 24 --output orbit-local-qa.mp4`.

## HyperFrames workflow (official engine, planned final gate)

Requirements: Node.js 22+, FFmpeg and Chromium. Run in the directory holding `index.html`:

```
npx hyperframes lint
npx hyperframes check --json
npx hyperframes snapshot --at 0,0.75,1.7,2.8,4.2,5.7
npx hyperframes preview
npx hyperframes render --quality draft -o orbit-hyperframes-draft.mp4
```

Root composition: `<div data-composition-id="bg-cover-orbit-v1" data-width="720" data-height="1280" data-duration="5.8" data-fps="24">`. All 24 images preload before `window.__hf.buildReady['bg-orbit-images']` resolves; `hf-seek` and `window.seekTo(t)` update geometry from absolute time, including 3D camera motion. Normal realtime RAF stops changing frames when the renderer begins deterministic seeking. **Never swap HyperFrames without checking its actual behavior.**

The repository workflow `.github/workflows/orbit-v1-preview.yml` attempts a HyperFrames render and falls back to the local Playwright/FFmpeg capture if that renderer fails; output is a downloadable GitHub Actions artifact. Check the logged rendering path. Playwright fallback is a *diagnostic*, not creative approval.

## Motion decisions

Four depth strata of square 3D cover meshes with actual card edges/backing, nonuniform independent angular velocities, elliptical trajectories with Z waves, camera truck/dolly/bank, soft lighting and depth attenuation. Four timed foreground flybys introduce changing focal points. Unlike the existing landing page's 2D elliptical CSS orbit, these cards use a real perspective projection, depth buffer and explicit camera coordinates in WebGL. The authored paths are original studies, **not traced** from the Apple reference.

## Hard limits / review gate

1. The approved Apple Music original MP4 is **not stored** in MarketingBeatGaler or BeatGaler. Its Instagram URL and descriptive notes exist, but timing/easing/lighting of the actual six seconds cannot be verified; do not claim visual parity.
2. The sandbox used for initial iteration had **no WebGL** and could not install npm packages due network restrictions. Preliminary screenshots used synthetic placeholders and the Canvas2D fallback, not the original covers or HyperFrames. These are sufficient to spot spacing/continuity defects, not to approve the final render.
3. Before proceeding to any more scenes, inspect a rendered MP4 using the **real covers**, compare sampled frames against the source Apple MP4 when provided, check camera path, true WebGL output, occlusion, edge artifacts, legibility and timing. Record user approval.
4. No modifications to the BeatGaler application, production, `main` branch or narration.

Sources: [HyperFrames GitHub](https://github.com/heygen-com/hyperframes), [HyperFrames CLI skill](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/SKILL.md), [Motion reference inventory](../../design-references/FIRST-VIDEO-REFERENCES.md).