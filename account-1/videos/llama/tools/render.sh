#!/usr/bin/env bash
# Renderiza el video completo. Desde la raiz del repo:
#   bash account-1/videos/llama/tools/render.sh
# Requiere Python 3.10+ (numpy, opencv-python, Pillow), FFmpeg y la fuente Inter (INTER_DIR=/ruta si no esta en /usr/share/fonts/opentype/inter).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p out
python3 tools/prepare.py
# Una escena por archivo, en paralelo. Rangos en frames a 30 fps (ver README, linea de tiempo).
python3 project/render.py desk 0 85 &
python3 project/render.py guy 85 154 &
python3 project/render.py bg 154 441 &
wait
for s in desk guy bg; do test -f "out/$s.mp4" || { echo "fallo la escena $s" >&2; exit 1; }; done
printf "file desk.mp4\nfile guy.mp4\nfile bg.mp4\n" > out/list.txt
ffmpeg -v error -y -f concat -i out/list.txt -c copy out/silent.mp4
# maxrate 8M: a 16 Mbps el reproductor del telefono se atoraba.
ffmpeg -v error -y -i out/silent.mp4 -i out/audio.wav -map 0:v -map 1:a \
  -c:v libx264 -crf 22 -maxrate 8M -bufsize 12M -preset medium -profile:v high -level 4.1 -g 30 -pix_fmt yuv420p -r 30 \
  -c:a aac -b:a 192k -ar 44100 -shortest -movflags +faststart out/llama.tmp.mp4
mv out/llama.tmp.mp4 out/llama.mp4
echo "listo: $(pwd)/out/llama.mp4"
