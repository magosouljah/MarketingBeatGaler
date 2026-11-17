#!/usr/bin/env bash
# Renderiza el anuncio completo (12.9 s) y su copia con contador de frames.
#
#   BEATGALER_REPO=/ruta/a/beatgaler bash account-1/videos/fuck/tools/render.sh
#
# Cinco tramos en paralelo (uno por escena) que se unen sin recodificar; el audio se mezcla aparte.
# Para cambiar una escena basta volver a renderizar su tramo: SEGMENTS="s4" bash .../render.sh
# Variables opcionales: CHROME=/ruta/a/chrome, PORT=8765.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"; ROOT="$(cd "$HERE/../../.." && pwd)"
PROJECT="$HERE/project"; OUT="$HERE/out"; PORT="${PORT:-8765}"
mkdir -p "$OUT"
[ -f "$PROJECT/assets/cloud.png" ] && [ -f "$OUT/mix.wav" ] || python3 "$HERE/tools/prepare.py"

( cd "$PROJECT" && exec python3 -m http.server "$PORT" >/dev/null 2>&1 ) & SERVER=$!
trap 'kill $SERVER 2>/dev/null || true' EXIT
sleep 1
export BASE_URL="http://127.0.0.1:$PORT/index.html"

# Tramos en tiempo de video: basura, notas+nube, explosion+galeria, share, CTA.
declare -A SEG=( [s1]="0 3.3" [s2]="3.3 6.0" [s3]="6.0 8.6" [s4]="8.6 10.6" [s5]="10.6 12.9" )
PIDS=()
for S in ${SEGMENTS:-s1 s2 s3 s4 s5}; do
  python3 "$HERE/tools/render.py" seg "$OUT/$S.mp4" ${SEG[$S]} & PIDS+=($!)
done
wait "${PIDS[@]}"   # no un `wait` a secas: tambien esperaria al servidor y no terminaria nunca
for S in s1 s2 s3 s4 s5; do [ -f "$OUT/$S.mp4" ] || { echo "Falta $OUT/$S.mp4" >&2; exit 1; }; echo "file '$S.mp4'"; done > "$OUT/list.txt"
ffmpeg -v error -y -f concat -i "$OUT/list.txt" -c copy "$OUT/video.mp4"
ffmpeg -v error -y -i "$OUT/video.mp4" -i "$OUT/mix.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest -movflags +faststart "$OUT/fuck.tmp.mp4"
mv "$OUT/fuck.tmp.mp4" "$OUT/fuck.mp4"
bash "$ROOT/shared/ffmpeg/review_copy.sh" "$OUT/fuck.mp4" "$OUT/fuck-frames.mp4"
echo "OK  $OUT/fuck.mp4"
