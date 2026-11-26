#!/usr/bin/env bash
# Render completo de esta variante:  bash tools/render.sh   (ID y duracion salen de project/js/variant.js)
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"; OUT="$HERE/out"; REPO="$(cd "$HERE/../../.." && pwd)"
rd(){ python3 -c "import json;print(json.loads(open('$HERE/project/js/variant.js').read().split('window.V = ',1)[1].rstrip().rstrip(';'))['$1'])"; }
ID=$(rd ID); DUR=$(rd DUR)
export HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1
HF="npx --yes hyperframes@0.9.44"; mkdir -p "$OUT"
[ -f "$HERE/project/assets/gsap.min.js" ] || bash "$HERE/tools/prepare.sh"
sed -i "s/data-duration=\"[0-9.]*\"/data-duration=\"$DUR\"/g" "$HERE/project/index.html"
cd "$HERE/project"; $HF lint
$HF render --fps 30 -o "$OUT/video.tmp.mp4" --quiet; mv "$OUT/video.tmp.mp4" "$OUT/video.mp4"
python3 "$HERE/tools/mix.py" "$OUT/audio.m4a"
ffmpeg -v error -y -i "$OUT/video.mp4" -i "$OUT/audio.m4a" -map 0:v -map 1:a -c copy -shortest -movflags +faststart "$OUT/placements-$ID.mp4"
bash "$REPO/shared/ffmpeg/review_copy.sh" "$OUT/placements-$ID.mp4" "$OUT/placements-$ID-frames.mp4"
