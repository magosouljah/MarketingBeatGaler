#!/usr/bin/env bash
# Render completo:  bash tools/render.sh   -> out/old-beats-C-C1-H1.mp4 y copia con contador de frames
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"; OUT="$HERE/out"; REPO="$(cd "$HERE/../../.." && pwd)"; ID=${ID:-C-C1-H3}; DUR=${DUR:-26.57}
mkdir -p "$OUT"; [ -f "$HERE/project/assets/clip.png" ] || bash "$HERE/tools/prepare.sh"
python3 "$HERE/tools/render.py" seg "$OUT/video.mp4" 0 "$DUR"
python3 "$HERE/tools/mix.py" "$OUT/audio.m4a"
ffmpeg -v error -y -i "$OUT/video.mp4" -i "$OUT/audio.m4a" -map 0:v -map 1:a -c copy -shortest -movflags +faststart "$OUT/old-beats-$ID.mp4"
FONT="${FONT:-$HERE/project/assets/fonts/InterDisplay-Black.otf}" bash "$REPO/shared/ffmpeg/review_copy.sh" "$OUT/old-beats-$ID.mp4" "$OUT/old-beats-$ID-frames.mp4"
