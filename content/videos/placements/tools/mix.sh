#!/usr/bin/env bash
# Mezcla de audio de Placements A-C1-H1.  bash tools/mix.sh [fin_en_segundos] [salida.m4a]
# Voz centrada y arriba, beat presente y sin ducking brusco (preferencia del propietario).
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"; IN="$HERE/inputs"; SFX="$HERE/project/assets/sfx"
END="${1:-24.10}"; OUT="${2:-$HERE/out/audio.m4a}"
ST="aresample=44100,pan=stereo|c0=c0|c1=c0"
# tiempos: ver project/js/timing.js (HOOK.VO y VOB)
# efectos: clic 15 ms antes de cada toque/clic, whoosh en las tres transiciones
CL=(1.05 13.26 14.05 14.46 15.06 15.45 15.85 16.25 16.85 18.14); WH=(4.76 9.18 17.20 20.92)
ARGS=(); F=""; MIXIN=""; n=6
for c in "${CL[@]}"; do ms=$(python3 -c "print(int(($c-0.015)*1000))"); ARGS+=(-i "$SFX/click.wav"); F+="[$n:a]$ST,volume=1.0,adelay=$ms|$ms[x$n];"; MIXIN+="[x$n]"; n=$((n+1)); done
for w in "${WH[@]}"; do ms=$(python3 -c "print(int($w*1000))"); ARGS+=(-i "$SFX/whoosh1.wav"); F+="[$n:a]$ST,volume=0.4,adelay=$ms|$ms[x$n];"; MIXIN+="[x$n]"; n=$((n+1)); done
ffmpeg -v error -y -i "$IN/beat.wav" -i "$IN/hook.wav" -i "$IN/body.wav" -i "$IN/body.wav" -i "$IN/body.wav" -i "$IN/cta.mp3" "${ARGS[@]}" -filter_complex "$F\
[0:a]atrim=start=6.0,asetpts=PTS-STARTPTS,aresample=44100,volume=0.80,afade=t=in:st=0:d=0.02[m];\
[1:a]atrim=0:4.05,asetpts=PTS-STARTPTS,$ST,volume=2.0,adelay=850|850[h];\
[2:a]atrim=0:5.98,asetpts=PTS-STARTPTS,afade=t=out:st=5.93:d=0.05,$ST,volume=1.5,adelay=5100|5100[b1];\
[3:a]atrim=5.98:9.20,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.03,afade=t=out:st=3.17:d=0.05,$ST,volume=1.5,adelay=11380|11380[b2];\
[4:a]atrim=9.20:11.69,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.03,$ST,volume=1.5,adelay=17120|17120[b3];\
[5:a]$ST,volume=1.4,adelay=21150|21150[ct];\
[m][h][b1][b2][b3][ct]$MIXIN amix=inputs=$n:normalize=0:duration=first,alimiter=limit=0.95,afade=t=out:st=$(python3 -c "print($END-0.18)"):d=0.18[out]" \
  -map "[out]" -t "$END" -ar 44100 -c:a aac -b:a 256k "$OUT"
echo "OK $OUT"
