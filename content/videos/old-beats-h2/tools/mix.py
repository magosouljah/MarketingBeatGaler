#!/usr/bin/env python3
"""Mezcla de la variante:  python tools/mix.py [salida.m4a]
Los beats van fuertes; bajo la voz solo ceden un poco y con rampas lentas (sin bombeo). Tiempos = project/js/timing.js."""
import subprocess, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent.parent; IN=HERE/"inputs"; SFX=HERE/"project/assets/sfx"
OUT=sys.argv[1] if len(sys.argv)>1 else str(HERE/"out/audio.m4a")
# ---- lo que cambia por variante (mismos numeros que project/js/variant.js) ----
HOOK,HOOK_DUR="C-H2",3.64
OLD0,NEW0,OLD=9.50,4.02,6.93
RCLICK,OPEN,NOTE1=5.75,6.15,6.30
WHOOSH=((2.2,"whoosh_a.wav",.35),(4.3,"whoosh_b.wav",.23))      # pico en los giros de camara de la intro
# ---------------------------------------------------------------------------
LOOP=OLD+(15.04-OLD0); D=LOOP+(16.73-11.346); DUR=D+(15.40-NEW0); WH=D+(10.74-NEW0)
VO=[(HOOK,0.0,HOOK_DUR),("C-C1a",HOOK_DUR+.05,5.86),("C-C1b",D-6.10,3.28),("C-C1c",D-2.70,2.60),("C-CTA",WH+.02,3.45)]
VO_GAIN,BEAT_SOLO,BEAT_UNDER,CLICK_GAIN,WHOOSH_GAIN=3.6,0.92,0.60,0.35,0.26
ms=lambda t:int(round(t*1000)); ST="aresample=48000,pan=stereo|c0=c0|c1=c0"
ins=[]; f=[]
def add(path,chain,t,tag):
    n=len(ins); ins.append(path); d=ms(max(0,t)); f.append(f"[{n}:a]{chain},adelay={d}|{d}[{tag}]"); return f"[{tag}]"
b =add(IN/"beat_viejo.mp4",f"atrim={OLD0}:15.04,asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.03,afade=t=out:st={15.04-OLD0-.012}:d=0.012",OLD,"b1")
b+=add(IN/"beat_viejo.mp4",f"atrim=11.346:16.73,asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.004,afade=t=out:st={16.73-11.346-.05}:d=0.05",LOOP,"b2")
b+=add(IN/"beat_nuevo.mp4",f"atrim={NEW0}:15.40,asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={15.40-NEW0-.35}:d=0.35",D,"b3")
# envolvente: 1 = hay voz encima. Frases seguidas se funden en un solo tramo.
spans=[]
for _,t,d in VO:
    if spans and t-spans[-1][1]<0.6: spans[-1][1]=t+d
    else: spans.append([t,t+d])
duck="+".join(f"clip((t-{a-.4:.2f})/0.4,0,1)*clip(({z+.5:.2f}-t)/0.5,0,1)" for a,z in spans)
f.append(f"{b}amix=inputs=3:normalize=0:duration=longest,volume=eval=frame:volume='{BEAT_SOLO}-{BEAT_SOLO-BEAT_UNDER}*min(1,{duck})'[beats]")
mix="[beats]"
for k,(name,t,_) in enumerate(VO): mix+=add(IN/f"{name}.wav",f"{ST},volume={VO_GAIN},alimiter=limit=0.9:attack=3:release=60",t,f"v{k}")
for k,t in enumerate((RCLICK,OPEN,D-6.10+1.70,D)): mix+=add(SFX/"click.wav",f"{ST},volume={CLICK_GAIN}",t-.015,f"c{k}")
mix+=add(SFX/"startup.wav","aresample=48000,volume=0.6",NOTE1,"st")
for k,(t,name,pk) in enumerate(WHOOSH+((WH-.3,"whoosh_b.wav",.23),)): mix+=add(SFX/name,f"aresample=48000,volume={WHOOSH_GAIN}",t-pk,f"w{k}")
n=mix.count("[")
f.append(f"{mix}amix=inputs={n}:normalize=0:duration=longest,alimiter=limit=0.89:attack=2:release=80:level=0[out]")
cmd=["ffmpeg","-v","error","-y"]+sum((["-i",str(p)] for p in ins),[])+["-filter_complex",";".join(f),"-map","[out]","-t",f"{DUR:.3f}","-ar","48000","-c:a","aac","-b:a","256k",OUT]
subprocess.run(cmd,check=True); print("OK",OUT,f"{DUR:.2f}s")
