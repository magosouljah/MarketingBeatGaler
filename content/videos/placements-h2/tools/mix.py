#!/usr/bin/env python3
"""Mezcla de audio leyendo project/js/variant.js:  python tools/mix.py [salida.m4a]
Voz arriba, beat presente y sin ducking; efectos discretos (clic 15 ms antes de cada toque, whoosh en transiciones)."""
import json, subprocess, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent.parent; IN=HERE/"inputs"; SFX=HERE/"project/assets/sfx"
V=json.loads((HERE/"project/js/variant.js").read_text().split("window.V = ",1)[1].rstrip().rstrip(";"))
A,H,S,C,END=V["AUDIO"],V["HOOK"],V["S"],V["C"],V["DUR"]; B=H["DUR"]
OUT=sys.argv[1] if len(sys.argv)>1 else str(HERE/"out/audio.m4a")
CLICK_GAIN, WHOOSH_GAIN = 0.40, 0.42          # efectos bajados a peticion del propietario (2026-11-25)
ST="aresample=44100,pan=stereo|c0=c0|c1=c0"; ms=lambda t:int(round(t*1000))
ins=[IN/A["beat"],IN/A["hook"],IN/"body.wav",IN/"body.wav",IN/"body.wav",IN/"cta.mp3"]
f=[f"[0:a]atrim=start={A['beatStart']},asetpts=PTS-STARTPTS,aresample=44100,volume={A.get('beatGain',0.8)},afade=t=in:st=0:d=0.03[m]",
   f"[1:a]atrim=0:{A['hookTrim']},asetpts=PTS-STARTPTS,{ST},volume={A['hookGain']},adelay={ms(H['VO'])}|{ms(H['VO'])}[h]",
   f"[2:a]atrim=0:5.98,asetpts=PTS-STARTPTS,afade=t=out:st=5.93:d=0.05,{ST},volume=1.5,adelay={ms(B)}|{ms(B)}[b1]",
   f"[3:a]atrim=5.98:9.20,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.03,afade=t=out:st=3.17:d=0.05,{ST},volume=1.5,adelay={ms(B+6.28)}|{ms(B+6.28)}[b2]",
   f"[4:a]atrim=9.20:11.69,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.03,{ST},volume=1.5,adelay={ms(V['SEG3'])}|{ms(V['SEG3'])}[b3]",
   f"[5:a]{ST},volume=1.4,adelay={ms(C['VO'])}|{ms(C['VO'])}[ct]"]
mixin="[m][h][b1][b2][b3][ct]"; n=6
for t in [H["SEND"]]+[S[k] for k in ("TAG1","TAG2","SEL0","SEL1","SEL2","SEL3","PACK","COPY","SENDL")]:
    ins.append(SFX/"click.wav"); d=ms(t-.015); f.append(f"[{n}:a]{ST},volume={CLICK_GAIN},adelay={d}|{d}[x{n}]"); mixin+=f"[x{n}]"; n+=1
# el pico del whoosh (56 % / 50 % de su duracion) cae en el momento del corte
for t,name,pk in ((H["WHIP"]+.12,"whoosh_a.wav",.35),(S["TAKE"]+.05,"whoosh_a.wav",.35),(S["BACK"]+.06,"whoosh_a.wav",.35),(C["T"]+.1,"whoosh_b.wav",.23)):
    ins.append(SFX/name); d=ms(max(0,t-pk)); f.append(f"[{n}:a]aresample=44100,volume={WHOOSH_GAIN},adelay={d}|{d}[x{n}]"); mixin+=f"[x{n}]"; n+=1
f.append(f"{mixin}amix=inputs={n}:normalize=0:duration=first,alimiter=limit=0.95,afade=t=out:st={END-.18}:d=0.18[out]")
cmd=["ffmpeg","-v","error","-y"]+sum((["-i",str(p)] for p in ins),[])+["-filter_complex",";".join(f),"-map","[out]","-t",str(END),"-ar","44100","-c:a","aac","-b:a","256k",OUT]
subprocess.run(cmd,check=True); print("OK",OUT)
