#!/usr/bin/env bash
# Renderiza add-finder completo: version negra (beat + voz + efectos) y blanca (solo voz).
#
#   bash content/videos/add-finder/tools/render.sh
#
# Variables opcionales:
#   THEMES="dark light"   que versiones renderizar
#   END=11.9  SPLIT=7.8   duracion total y punto de corte entre los dos tramos
#   HYPERFRAMES_BROWSER_PATH=/ruta/a/chrome   si HyperFrames no puede bajar su navegador
#
# El video se renderiza en dos tramos y se une sin recodificar: ~0.7 s por frame en 2 CPU,
# asi que un tramo de 8 s tarda unos 3 minutos. El audio se mezcla aparte con FFmpeg.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT="$HERE/project"; OUT="$HERE/out"; A="$PROJECT/assets"
HF="npx --yes hyperframes@0.9.44"
export HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1
THEMES="${THEMES:-dark light}"; END="${END:-11.9}"; SPLIT="${SPLIT:-7.8}"
mkdir -p "$OUT"

[ -f "$A/gsap.min.js" ] && [ -f "$A/vo/l3.wav" ] && [ -d "$A/covers" ] || python3 "$HERE/tools/prepare.py"

cd "$PROJECT"
$HF lint

restore_theme() { printf '// Tema del render: "dark" (version negra) o "light" (version blanca).\n// tools/render.sh reescribe este archivo antes de cada render.\nwindow.BG_THEME = "dark";\n' > "$PROJECT/theme.js"; }
trap restore_theme EXIT

MUSIC_END=$(python3 -c "print(0.546+$END)")
for THEME in $THEMES; do
  NAME=$([ "$THEME" = light ] && echo blanco || echo negro)
  printf 'window.BG_THEME = "%s";\n' "$THEME" > "$PROJECT/theme.js"
  $HF render --start 0 --end "$SPLIT" --fps 30 -o "$OUT/$NAME-a.tmp.mp4" --quiet
  $HF render --start "$SPLIT" --end "$END" --fps 30 -o "$OUT/$NAME-b.tmp.mp4" --quiet
  mv "$OUT/$NAME-a.tmp.mp4" "$OUT/$NAME-a.mp4"; mv "$OUT/$NAME-b.tmp.mp4" "$OUT/$NAME-b.mp4"
  printf "file '%s'\nfile '%s'\n" "$NAME-a.mp4" "$NAME-b.mp4" > "$OUT/$NAME-concat.txt"
  ffmpeg -v error -y -f concat -safe 0 -i "$OUT/$NAME-concat.txt" -an -c:v copy "$OUT/$NAME-video.mp4"

  ST="pan=stereo|c0=c0|c1=c0"
  if [ "$THEME" = light ]; then
    # Version blanca: solo las cuatro frases de voz.
    ffmpeg -v error -y -i "$A/vo/l1a.wav" -i "$A/vo/l1b.wav" -i "$A/vo/l2.wav" -i "$A/vo/l3.wav" -filter_complex \
"[0:a]aresample=44100,$ST,volume=1.5,adelay=300|300[a1];[1:a]aresample=44100,$ST,volume=1.5,adelay=2500|2500[a2];\
[2:a]aresample=44100,$ST,volume=2.0,adelay=5020|5020[a3];[3:a]aresample=44100,$ST,volume=1.9,adelay=8630|8630[a4];\
[a1][a2][a3][a4]amix=inputs=4:normalize=0:duration=longest,apad=whole_dur=$END,alimiter=limit=0.95[out]" \
      -map "[out]" -t "$END" -ar 44100 -c:a aac -b:a 256k "$OUT/$NAME-audio.m4a"
  else
    # Version negra: el beat entra desde 0.546 s del archivo para que su kick de 5.346 s caiga en el clic (4.80 s),
    # baja bajo la voz final y cierra con fundido. Clics en 4.785, 8.056 y 10.915 s; whooshes en 0.8 y 8.12 s.
    ffmpeg -v error -y -i "$A/beat.mp3" -i "$A/vo/l1a.wav" -i "$A/vo/l1b.wav" -i "$A/vo/l2.wav" -i "$A/vo/l3.wav" \
      -i "$A/sfx/click.wav" -i "$A/sfx/click.wav" -i "$A/sfx/click.wav" -i "$A/sfx/whoosh1.wav" -i "$A/sfx/whoosh2.wav" -filter_complex \
"[0:a]atrim=0.546:$MUSIC_END,asetpts=PTS-STARTPTS,volume='if(lt(t,8.5),0.85,if(lt(t,8.65),0.85-(t-8.5)/0.15*0.35,0.50))':eval=frame,afade=t=out:st=11.35:d=0.55[m];\
[1:a]aresample=44100,$ST,volume=1.6,adelay=300|300[a1];[2:a]aresample=44100,$ST,volume=1.6,adelay=2500|2500[a2];\
[3:a]aresample=44100,$ST,volume=2.5,adelay=5020|5020[a3];[4:a]aresample=44100,$ST,volume=2.3,adelay=8630|8630[a4];\
[5:a]$ST,volume=1.3,adelay=4785|4785[c1];[6:a]$ST,volume=1.3,adelay=8056|8056[c2];[7:a]$ST,volume=1.3,adelay=10915|10915[c3];\
[8:a]$ST,volume=0.5,adelay=800|800[w1];[9:a]atempo=2.4,$ST,volume=0.33,adelay=8120|8120[w2];\
[m][a1][a2][a3][a4][c1][c2][c3][w1][w2]amix=inputs=10:normalize=0:duration=first,alimiter=limit=0.95[out]" \
      -map "[out]" -t "$END" -ar 44100 -c:a aac -b:a 256k "$OUT/$NAME-audio.m4a"
  fi
  ffmpeg -v error -y -i "$OUT/$NAME-video.mp4" -i "$OUT/$NAME-audio.m4a" -map 0:v -map 1:a -c:v copy -c:a copy -shortest -movflags +faststart "$OUT/add-finder-$NAME.tmp.mp4"
  mv "$OUT/add-finder-$NAME.tmp.mp4" "$OUT/add-finder-$NAME.mp4"
  echo "OK  $OUT/add-finder-$NAME.mp4"
done
