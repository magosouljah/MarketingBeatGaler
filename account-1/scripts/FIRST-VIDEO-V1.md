# BeatGaler — First product video (working brief)

Status: concept and narration V3 approved as working baseline; visuals exploratory, **no final motion approved**. Target: vertical 9:16, cinematic/premium product advertisement, approximately 30–35 seconds pending recorded narration. English female narrator, deep cinematic tone with energetic moments. Work voice-first for timing, but approve one high-fidelity visual before full production.

## Narration — V3 (preserve unless user requests changes)

1. You probably have hundreds of beats with weird names.
2. You make one. Save it. Make another.
3. But when you're looking for that one beat...
4. Which one is it?
5. What if your beats were more than just filenames?
6. Introducing BeatGaler.
7. Unlimited cloud storage for your beats.
8. Give them cover art.
9. Rate your favorites.
10. Organize them by genre and tags.
11. Everything in one place.
12. BeatGaler.
13. Create ur Galer.

## Core creative logic

Pain: beatmakers may have many vaguely named files, so recognizing, previewing and categorizing a beat is difficult. Do **not** claim beats were lost. Solution: visual cover art, ratings, genres/tags and immediate playback, shown through actual BeatGaler interface. Show playback visually, not necessarily in voiceover. Visual continuity matters more than one scene per sentence.

## Storyboard (working, not final)

- 1–2: Windows-style file explorer crowded with oddly named WAV files; as producer saves more, files multiply rhythmically. Avoid a long boring screen recording or FL Studio save tutorial.
- 3–4: Quickly try playing two indistinguishable WAV files, close incorrect snippets, pull back to a sea of names, short pause on 'Which one is it?'. This concept is **not approved** and needs redesign/testing.
- 5: **Hero transformation**: audio files organically mutate at different speeds; cover art, ratings and colored tags grow out of them; cards gain dimensionality and enter cinematic 3D orbit. Not a basic crossfade or instant substitution.
- 6: Reveal BeatGaler landing and orbiting cover art briefly, no static hold.
- 7: Same covers flow into actual BeatGaler gallery grid, continuous camera move.
- 8: Drag a photo onto an existing grey/default-cover BeatCard, replace cover.
- 9: Focus card and adjust star rating; card returns to gallery.
- 10: Filter tags, then play different beats and synchronize soundtrack with environmental effects. R&B: warm pink romance, flowers/petals. Dark: screen darkens except circular flashlight spotlight. Tropical: sun, stylized wave/water reflection, beach feeling. Filter selection ~1.5 s, three moods ~1 s each, ending ~0.5 s; total ~5 s **hypothesis** requiring testing. Do not accidentally imply three genre tags are selected simultaneously if the real filter intersects tags.
- 11: Pull back; cards unify into composition.
- 12–13: Minimal brand ending and white 'Create ur Galer' CTA. Avoid repetitive full landing reveal if #6 already showed it.

## Preliminary timing (unvalidated)

0–10 s problem; 10–18 s mutation/orbit; 18–30 s product demonstration; 30–35 s brand ending. Actual voiceover and animatic must determine duration; previous synthetic animatic ~30.3 s was too low fidelity to assess creative quality.

## Creative reference and design

Apple Music reference: short (~6 s) cinematic 3D orbit of cover art, continuous camera and intentional composition; user likes that the existing BeatGaler landing already has orbiting covers. Other user-supplied social videos emphasize premium motion and product demos. References listed in REFERENCES.md; original MP4s are **not** committed. Use actual BeatGaler cover assets and authentic product UI. Avoid generic template/PowerPoint visuals.

## Prior attempts and feedback

- Low-fidelity animatic with robotic placeholder voice: rejected as unhelpful for visual-quality evaluation.
- A 6 s code-generated orbit video: emphatically rejected as very poor. Root causes: mostly flat composition, uniform motion, simplistic file-to-card substitutions, insufficient lighting/depth/camera choreography, no shot-by-shot reference analysis or quality gate. **Do not reuse or claim this is approved.** MP4 files were delivered in ChatGPT but are not in GitHub.
- User specifically requested research into professional code-driven motion tools and the existing marketing repository. Research recovered the already-approved renderer decision: **HeyGen HyperFrames**, with HTML/CSS/JS, potentially Three.js and GSAP. Do not switch renderers without measured evidence; see FASE-0.md.

## Next milestone — ONE high-fidelity graphic, not whole ad

1. Inspect README.md, PLAN.md, FASE-0.md, shared/README.md and HyperFrames official docs/skills.
2. Obtain and actually inspect Apple Music video reference frame-by-frame (camera path, timing, depth, object trajectories, easing, lighting, composition); request original file if not available in new environment. Do not pretend reference MP4s are in repository.
3. Source actual BeatGaler covers from existing design assets; preserve aspect, texture, typography and visual language.
4. Implement a standalone **web-page preview** of just the 3D cover orbit (not file mutation or entire 5–7 sequence yet) using HyperFrames and appropriate 3D tooling. Preview interactively and render a short test clip.
5. Self-review sampled frames and motion; compare against reference. No claims of cinematic parity without evidence.
6. Share a playable MP4 and preview or screenshots accessible from mobile. Iterate until user approves orbit. Then add organic file-to-card transformation and transition to landing.

No changes to BeatGaler production or deployment. Keep video project in MarketingBeatGaler; avoid modifying main app except read-only asset discovery. User approval is creative gate.
