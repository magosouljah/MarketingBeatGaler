#!/usr/bin/env bash
# Deja project/assets listo: portadas compartidas, gsap, fuentes, grano, e imagenes del chat desde inputs/.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"; REPO="$(cd "$HERE/../../.." && pwd)"; A="$HERE/project/assets"
mkdir -p "$A/covers" "$A/ig" "$A/fonts"
cp "$REPO"/content/assets/covers/cover-*.jpg "$A/covers/"
cp "$REPO/content/videos/add-finder/project/assets/fonts/InterDisplay-Black.otf" "$A/fonts/"
cp "$REPO/content/videos/add-finder/project/assets/grain.png" "$A/"
( cd "$HERE/project" && npm install --silent gsap@3.13.0 && cp node_modules/gsap/dist/gsap.min.js assets/ )
ffmpeg -v error -y -i "$HERE/inputs/story.jpg" -q:v 2 "$A/ig/story.jpg"
ffmpeg -v error -y -i "$HERE/inputs/avatar.jpg" -vf scale=300:300 -q:v 2 "$A/ig/avatar.jpg"
# los iconos .flp/.als ya estan versionados en project/assets/icons (capturas del propietario, 2026-11-25)
echo "assets listos"
