#!/usr/bin/env bash
# Deja project/assets listo: frames de las dos grabaciones de FL, sprite del clip, mascara del carril, fuentes, portadas e iconos.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"; REPO="$(cd "$HERE/../../.." && pwd)"; A="$HERE/project/assets"; IN="$HERE/inputs"
OLD0=${OLD0:-7.65}; NEW0=${NEW0:-5.70}        # segundo del archivo donde empieza a usarse cada grabacion (compas medido)
mkdir -p "$A"/{fl/viejo,fl/nuevo,fonts,covers,icons,gcovers,sfx}
ffmpeg -v error -y -ss $OLD0 -i "$IN/beat_viejo.mp4" -vf fps=30 -q:v 3 "$A/fl/viejo/%04d.jpg"
ffmpeg -v error -y -ss $NEW0 -i "$IN/beat_nuevo.mp4" -vf fps=30 -q:v 3 "$A/fl/nuevo/%04d.jpg"
cp "$REPO"/content/videos/wheel/lab-v2/hyperframes/assets/covers/* "$A/covers/"          # la rueda las pide con estos nombres
cp "$REPO"/content/videos/wheel/lab-v2/hyperframes/assets/fonts/* "$A/fonts/"
cp "$REPO"/content/videos/placements/project/assets/fonts/* "$A/fonts/"
cp "$REPO/content/videos/add-finder/project/assets/fonts/InterDisplay-Black.otf" "$A/fonts/"
cp "$REPO"/content/videos/placements/project/assets/icons/*.png "$A/icons/"
cp "$REPO"/content/videos/placements/project/assets/sfx/*.wav "$A/sfx/"
cp "$REPO"/content/assets/covers/cover-0*.jpg "$A/gcovers/"
( cd "$HERE/project" && [ -f assets/fonts/caveat-latin-700-normal.woff2 ] || { npm install --silent --no-save @fontsource/caveat@5 && cp node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2 assets/fonts/ && rm -rf node_modules package-lock.json; } )
python3 "$HERE/tools/sprites.py" ${LIFT_F:-242}
python3 "$HERE/tools/make_sfx.py"
echo "assets listos: $(ls "$A/fl/viejo" | wc -l) + $(ls "$A/fl/nuevo" | wc -l) frames"
