#!/usr/bin/env python3
"""Calcula project/js/variant.js para un hook y un beat nuevos, sin tocar el cuerpo.

    python tools/sync.py            # lee variant.def.json (junto a README.md) y inputs/

Que hace:
  1. Mide kicks y cajas del beat (shared/editing/find_hits.py).
  2. Busca desde que punto del beat debe entrar la musica para que los momentos clave del cuerpo
     (despegue, caida en la rejilla, clics de tags, pack, link, vuelta al chat, FIRE, GALER) caigan sobre golpes.
  3. Ajusta cada accion libre al golpe medido mas cercano (max. ~0.15 s), respetando el orden,
     la separacion minima entre clics y las palabras de la voz, que no se mueven.
Los tiempos del hook (V.HOOK) vienen del .def y se disenan a mano contra la alineacion de palabras."""
import json, re, subprocess, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent.parent; REPO=HERE.parent.parent.parent
D=json.loads((HERE/"variant.def.json").read_text()); H=D["HOOK"]; B=H["DUR"]
FH=next(p for p in [REPO/"shared/editing/find_hits.py",Path("/home/claude/marketingbeatgaler/shared/editing/find_hits.py")] if p.exists())
out=subprocess.run([sys.executable,str(FH),str(HERE/"inputs"/D["AUDIO"]["beat"]),"--umbral","0.35"],capture_output=True,text=True).stdout
ons=[]; kind=None
for ln in out.splitlines():
    if ln.startswith("KICK"): kind=1.0
    elif ln.startswith("CAJA"): kind=0.7
    elif ln.startswith("ENERGIA"): kind=None
    else:
        m=re.match(r"\s*([\d.]+) s\s+fuerza ([\d.]+)",ln)
        if m and kind: ons.append((float(m[1]),float(m[2])*kind))
# rejilla de corcheas del beat (hats): golpes debiles donde no hay kick ni caja medidos
if D.get("GRID"):
    g=D["GRID"]; k=-int(g["phase"]/(g["beat"]/2))
    while g["phase"]+k*g["beat"]/2<40:
        t=g["phase"]+k*g["beat"]/2
        if t>=0 and not any(abs(o-t)<.06 for o,_ in ons): ons.append((round(t,3),.3 if k%2==0 else .2))
        k+=1
ons.sort(); LEN=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",str(HERE/"inputs"/D["AUDIO"]["beat"])],capture_output=True,text=True).stdout)
# tiempos nominales del cuerpo, relativos a B (los de A-C1-H1 aprobado)
N=dict(HUN=1.77,TAKE=4.15,LAND=5.75,TAG1=8.16,TAG2=8.95,SEL0=9.36,SEL1=9.96,SEL2=10.35,SEL3=10.75,PACK=11.15,COPY=11.75,BACK=12.15,SENDL=13.04,READY2=13.94,FIRE=14.56,GALER=15.81)
Wt=dict(HUN=1.5,TAKE=2,LAND=3,TAG1=2,TAG2=1.5,SEL0=1,SEL1=.5,SEL2=.5,SEL3=.5,PACK=1.5,COPY=1.5,BACK=2,SENDL=1,READY2=1,FIRE=3,GALER=2)
ev=[(B+N[k],Wt[k]) for k in N]+[(H["SEND"],1),(H["MSG"],1.5)]
def near(t,tol):
    best=None
    for o,s in ons:
        d=abs(o-t)
        if d<=tol and (best is None or d<abs(best[0]-t)): best=(o,s)
    return best
def score(m):
    sc=0
    for t,w in ev:
        n=near(t+m,.12)
        if n: sc+=w*n[1]*(1-abs(n[0]-t-m)/.12)
    return sc
total=B+N["FIRE"]+0.79+2.95+.3
ms=[i*.005 for i in range(0,int(max(0,LEN-total)/.005)+1)]
m=max(ms,key=score); print(f"musica desde {m:.3f} s del archivo (puntuacion {score(m):.2f}; sin desfase {score(0):.2f})")
def snap(t,lo,hi,minT=None):
    """golpe mas fuerte-cercano en [t+lo, t+hi] (tiempo de video), o t si no hay"""
    c=[(o-m,s) for o,s in ons if t+lo<=o-m<=t+hi and (minT is None or o-m>=minT)]
    if not c: return max(t,minT) if minT else t
    return round(max(c,key=lambda x:x[1]-abs(x[0]-t)*3)[0],3)
S={}
S["TAKE"]=snap(B+N["TAKE"],-.15,.2); S["LAND"]=snap(B+N["LAND"],-.15,.15,S["TAKE"]+1.35)
S["TAG1"]=snap(B+N["TAG1"],-.05,.26); S["TAG2"]=snap(B+N["TAG2"],-.05,.22,S["TAG1"]+.6)
prev=S["TAG2"]; sh=0
for k,gap in (("SEL0",.38),("SEL1",.5),("SEL2",.34),("SEL3",.34),("PACK",.38),("COPY",.55),("BACK",.36)):
    S[k]=snap(B+N[k]+sh,-.14,.14,prev+gap); sh=S[k]-(B+N[k]); prev=S[k]
bk=S["BACK"]; S["PASTE"]=round(bk+.37,3); S["SENDL"]=snap(bk+.89,-.1,.12,S["PASTE"]+.4); S["DOTS2"]=round(S["SENDL"]+.46,3)
SEG3=round(bk-.13,3); ready2=SEG3+1.92
S["FIRE"]=snap(bk+2.41,-.1,.3,ready2+.38)
# CTA: GALER (0.54 s despues de C.T) sobre un golpe si lo hay
g=snap(S["FIRE"]+.71+.54,-.15,.3); T=round(g-.54,3); VO=round(T+.08,3)
C=dict(T=T,VO=VO,COMMENT=VO,GALER=round(VO+.46,3),TO=round(VO+1.46,3),FOR=round(VO+1.83,3),END=round(VO+1.94,3))
C["PULSE"]=snap(C["GALER"]+1.14,-.4,.4,C["GALER"]+.6); S["ACC"]=g
H["K"]=[round(o-m,3) for o,s in ons if .1<o-m<H["PULL"] and s>=.6 and abs(o-m-H["SEND"])>.1 and abs(o-m-H["MSG"])>.1][:4] or [0.05]
V=dict(ID=D["ID"],GLOW=D["GLOW"],HOOK=H,SEG3=SEG3,S=S,C=C,DUR=round(VO+2.95,2),AUDIO=dict(D["AUDIO"],beatStart=round(m,3)))
(HERE/"project/js/variant.js").write_text("// Escrito por tools/sync.py a partir de variant.def.json y del beat medido. No editar sin volver a medir.\nwindow.V = "+json.dumps(V,indent=1)+";\n")
for k in ("TAKE","LAND","TAG1","TAG2","SEL0","SEL1","SEL2","SEL3","PACK","COPY","BACK","SENDL","FIRE"):
    nom=B+N[k]+(S["BACK"]-(B+N["BACK"]) if k in("SENDL","FIRE") else 0); n=near(S[k]+m,.03)
    print(f"  {k:6s} {S[k]:7.3f}  ({S[k]-B-N[k]:+.2f} vs H1)  {('sobre golpe ' if n[1]>.3 else 'sobre la rejilla ')+format(n[1],'.2f') if n else 'sin golpe cerca'}")
print("  GALER",C["GALER"],"DUR",V["DUR"],"K",H["K"])
