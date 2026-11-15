#!/usr/bin/env bash
# Copia de revision con contador de frames quemado: "F 136   4.533333s".
#
#   bash shared/ffmpeg/review_copy.sh video.mp4 [salida.mp4]
#
# Regla validada (add-finder): toda prueba que se manda al propietario lleva esta copia,
# para que pueda decir "en F124 a F141 la mano va muy rapido" en vez de describirlo.
# El frame 0 es siempre el inicio del anuncio; si cambia el inicio, avisar que la numeracion se recorrio.
set -euo pipefail
IN="$1"; OUT="${2:-${IN%.*}-frames.mp4}"
FONT="${FONT:-$(fc-match -f '%{file}' 'Inter:bold' 2>/dev/null || true)}"
[ -n "$FONT" ] || { echo "No encontre una fuente; define FONT=/ruta/fuente.ttf" >&2; exit 1; }
ffmpeg -v error -y -i "$IN" \
  -vf "drawtext=fontfile=$FONT:text='F %{frame_num}   %{pts\:flt}s':start_number=0:x=40:y=h-120:fontsize=54:fontcolor=white:box=1:boxcolor=black@0.75:boxborderw=18" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a copy "$OUT.tmp.mp4"
mv "$OUT.tmp.mp4" "$OUT"
echo "OK  $OUT"
