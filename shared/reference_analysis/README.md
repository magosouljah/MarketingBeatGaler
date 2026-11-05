# Reference Analysis V1

Executable evidence preparation and agent-assisted technical study, not autonomous creative judgment. Python 3.10+ stdlib; FFmpeg and ffprobe on PATH (tested locally with FFmpeg 2025-10-05 build). No Python packages, cloud calls, subscriptions or downloaded models. Run from repository root.

```bash
python -m shared.reference_analysis.demo reference-runs/demo-input
python -m shared.reference_analysis.pipeline analyze reference-runs/demo-input/source.mkv reference-runs/demo-analysis --account account-1 --tracks reference-runs/demo-input/tracks.json
python -m shared.reference_analysis.pipeline validate reference-runs/demo-analysis
python -m shared.reference_analysis.pipeline register reference-runs/demo-analysis demo-reference-test
python learning/engine.py audit
python -m unittest discover -s learning/tests -v
python -m unittest discover -s shared/reference_analysis/tests -v
```

Use new output folders and case IDs on subsequent iterations. `reference-runs/` is ignored for private media; registration there is useful locally but those paths must be copied into explicitly selected, redistribution-permitted versioned evidence before committing cases. Never publish original third-party reference footage or its extracted frames merely to make a test reproducible. The committed synthetic example is authored by this project and can be regenerated.

## Input, limits and reproducibility

`analyze LOCAL_FILE NEW_FOLDER --account account-1|account-2 [--annotations notes.json] [--tracks tracks.json] [--max-seconds 60] [--max-frames 1800] [--cut-threshold 0.22]`

The pipeline hashes the source, probes streams and actual presentation timestamps, decodes every source frame into a 64×64 grayscale metric and a PNG at <=640px coded width. No FPS resampling or seek-per-image approximation. It rejects duplicate/nonmonotonic PTS and count mismatches. Variable frame intervals remain intact. PNG file number minus one is the source presentation frame index. First frame local time = 0; source PTS is preserved separately. Container duration and first-to-last-frame span are different quantities. Rotation is not applied; non-square pixel aspect and color tags remain in probe metadata for review. Thumbnail luma is not calibrated photometry or a color/material analysis.

Default limits: 60s, 1800 frames, 512MiB input, <=3840×2160 pixels, one decoder thread, 120s timeout per subprocess. Tools may use other internal threads; this is not a whole-machine hard resource quota. No network protocols are allowed inside input decoding. PNG extraction and low-resolution measurement require separate decodes. Defaults target short motion references; limits may be increased deliberately. Actual FPS determines frame coverage; a 60fps clip reaches the default frame limit at 30s. Oversized, unknown-duration or corrupt inputs fail; no partial output is published. Existing outputs are never overwritten. Temporary output is renamed into place only after validation. Interrupted runs may leave `.reference-*` scratch directories; these are not completed outputs.

Two runs with the same source, annotations and tool build should produce the same `analysis.json` and frame hashes; provenance paths may differ. Cross-build pixel identity is not guaranteed. Record versions and commands, pin tool builds when reproducing a comparison. Source bytes are hashed before/after processing to detect mutation.

## Output contract (schema_version = 1)

- `analysis.json`: source name/size/SHA256, account, video metadata, container duration, per-frame index/source PTS/local seconds/path/hash/luma/difference, estimated cut candidates, audio stream offsets, annotations, optional estimated tracks, warnings and limitations.
- `probe.json`, `frame-probe.json`: raw FFprobe evidence. `provenance.json`: versions and executed decode commands. Commands include local paths; review before publishing.
- `frames/000001.png…`: complete coded-orientation sequence; not a semantic segmentation.
- `report.md`: reproducibly generated technical report with measured, estimated and authored sections separated.
- `manifest.json`: hashes of all other files. `validate` checks exact file inventory, hashes, frame sequence, original probed PTS, annotation categories, track calculations, cut categories/times, and report consistency. Hashes detect accidental corruption, not malicious rewriting of every evidence file.

Candidate cuts are adjacent grayscale mean absolute difference >= threshold. A flash, fast pan or fade can confuse this heuristic; no claim of semantic scenes. Identical thumbnail warnings describe identical processed pixels; legitimate holds are not rejected as missing source frames. Gaps cannot be conclusively attributed to dropped frames without independent capture evidence.

Audio: inspect stream start offsets relative to first video PTS; flag unknown or >50ms offsets for inspection. Does not decode sound, identify beats, transcribe, validate lip sync or detect drift within a clip. Mark those dimensions unexamined until a separate timestamped listening test is supplied. The synthetic example tests the offset warning with an intentionally delayed audio stream.

## Authored evidence contract

`--annotations` accepts a JSON list, each with exactly:

```json
[{"id":"fan-out", "kind":"hypothesis", "start_frame":0, "end_frame":5,
  "claim":"Independent card rotations could produce the apparent spread",
  "evidence":"Name the inspected source frames and visible cues",
  "method":"State how the inference was made", "uncertainty":"Camera and object motion remain ambiguous"}]
```

Kinds: `observation`, `estimate`, `interpretation`, `hypothesis`. No authored `measurement` category. The software checks structure and range, not the truth of prose. Reviewers must reject interpretations disguised in observation text. Machine measurements have a fixed method and frame provenance.

`--tracks` accepts a list with exactly `id`, `evidence`, `uncertainty`, `samples`; each sample has `frame`, `x`, `y`. Coordinates are normalized to the coded image (right/down). Example generated by `demo`: square center at frames 0,10,20. Minimum two strictly increasing samples. Tracks and finite-difference velocity/acceleration remain estimates; acceleration compares segment velocities at segment temporal midpoints, accounting for VFR timing. Split tracks at cuts/occlusions/identity loss. Sparse samples do not prove an easing curve, hidden depth or camera motion. Generator-supplied demo points demonstrate arithmetic, not automatic tracking.

## Learning Engine integration

`register` validates a complete run inside the repository and creates a new immutable-ID case, `reference-integrity: pass`, `human_approved: false`, then calls the existing `learning.engine.review`. This pass is only technical artifact integrity. It does not establish source interpretation, creative quality, redistributability or validated knowledge.

For a failed experiment write a diagnostic and run:

```bash
python -m shared.reference_analysis.pipeline failure reference-example-failure path/to/diagnostic.json --account account-1
```

Required diagnostic strings: `check_id`, `evidence`, `cause_category`, `hypothesis`, `problem`, `implementation`, `use_when`, `avoid_when`, `acceptance_test`. Cause categories: `reference-interpretation`, `tool-choice`, `implementation`, `technical-knowledge`, `ambiguous-instructions`, `evaluation-process`. All causes remain hypotheses. The existing engine records evidence, creates a proposed rule with use/avoid conditions and acceptance test. Correction → new case → comparable evaluation; no automatic `promote`. Read `learning/README.md` for distinct verification and real creative approval gates. No changes to the engine's promotion logic.

## First case: Apple Music orbit

Original pointer: https://www.instagram.com/p/DcBoH7XgD1V/ . No original MP4 exists in this checkout or the inspected tracked remote trees. Historical analysis in branch `marketing/orbit-reference-rebuild-v3`, file `account-1/creative-assets/ORBIT-APPLE-REFERENCE-ANALYSIS.md`, reports prior access, but this run has not verified that footage or its numbers. Historical reconstructions were rejected. No unique 3D trajectory or camera can be recovered from those descriptions.

The synthetic test proves ingestion, source-frame coverage, known cut detection, hold warnings, optional 2D kinematics, report generation, integrity validation and Learning Engine integration. It does not test cinematic quality or orbit reconstruction. See [research](RESEARCH.md) for the next source-dependent experiment.
