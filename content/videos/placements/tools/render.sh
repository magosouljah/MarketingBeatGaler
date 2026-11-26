#!/usr/bin/env bash
# Render completo de Placements A-C1-H1:  bash content/videos/placements/tools/render.sh
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"; OUT="$HERE/out"; REPO="$(cd "$HERE/../../.." && pwd)"; NAME="placements-A-C1-H1"
export HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1
HF="npx --yes hyperframes@0.9.44"; END=24.10; mkdir -p "$OUT"
[ -f "$HERE/project/assets/gsap.min.js" ] || bash "$HERE/tools/prepare.sh"
cd "$HERE/project"; $HF lint
$HF render --fps 30 -o "$OUT/video.tmp.mp4" --quiet; mv "$OUT/video.tmp.mp4" "$OUT/video.mp4"
bash "$HERE/tools/mix.sh" "$END" "$OUT/audio.m4a"
ffmpeg -v error -y -i "$OUT/video.mp4" -i "$OUT/audio.m4a" -map 0:v -map 1:a -c copy -shortest -movflags +faststart "$OUT/$NAME.mp4"
bash "$REPO/shared/ffmpeg/review_copy.sh" "$OUT/$NAME.mp4" "$OUT/$NAME-frames.mp4"
