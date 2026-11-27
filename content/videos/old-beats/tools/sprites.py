#!/usr/bin/env python3
"""Recorta el clip de la melodia (ZENOLOGY, Track 1 del proyecto viejo) y el carril vacio que tapa Track 1 del proyecto nuevo.
Coordenadas medidas sobre las grabaciones 1920x1052; el clip se busca por plantilla para no depender del scroll."""
import json, sys
from pathlib import Path
import cv2, numpy as np
HERE=Path(__file__).resolve().parent.parent; A=HERE/"project/assets"
LIFT_F=int(sys.argv[1]) if len(sys.argv)>1 else 287       # frame (30 fps desde OLD0) en que el clip se despega
Y0,Y1=147,197; PLAYHEAD=792; FIX=8   # el icono de patron empieza 8 px antes del salto de brillo
old=cv2.imread(str(A/f"fl/viejo/{LIFT_F+1:04d}.jpg"))
row=old[Y0:Y0+17,683:1900]; g=cv2.cvtColor(row,cv2.COLOR_BGR2GRAY).astype(np.float32)
# inicios de clip: la cabecera es mas clara que la separacion entre clips; el icono de patron marca el inicio
ref=cv2.cvtColor(old[Y0:Y0+17,683:1900],cv2.COLOR_BGR2GRAY)
# plantilla: icono + "ZEN" del clip que esta bajo el cursor de reproduccion (buscado como el primer maximo a la izquierda)
col=g.mean(axis=0); starts=[]
tpl=None
for x in range(5,len(col)-60):
    pass
# busqueda directa por autocorrelacion con periodo de 8 compases
best=None
for x0 in range(0,260):
    seg=g[:,x0:x0+60]
    if seg.shape[1]<60: break
    res=cv2.matchTemplate(g,seg,cv2.TM_CCOEFF_NORMED)[0]
    peaks=[i for i in range(len(res)) if res[i]>.9 and res[i]==res[max(0,i-8):i+9].max()]
    if len(peaks)>=4:
        d=np.diff(peaks)
        if d.std()<1.5 and (best is None or res[peaks].mean()>best[0]) and 200<d.mean()<240:
            best=(res[peaks].mean(),peaks,d.mean())
assert best, "no encontre la rejilla de clips ZENOLOGY"
_,peaks,per=best
# borde izquierdo del clip: columna oscura de separacion justo antes del icono
edges=[]
for p in peaks:
    x=p
    while x>1 and col[x-1]>col[max(0,p-25):p+1].min()+6: x-=1
    edges.append(683+x)
per=float(per)
cand=[e for e in edges if e>PLAYHEAD+40]
x0=min(cand); x1=int(round(x0+per))
# afinar: el clip empieza donde la cabecera sube de brillo
hdr=cv2.cvtColor(old[Y0+2:Y0+12,x0-12:x0+12],cv2.COLOR_BGR2GRAY).mean(axis=0)
x0=x0-12+int(np.argmax(np.diff(hdr)))+1-FIX; x1=x0+int(round(per))
cv2.imwrite(str(A/"clip.png"),old[Y0:Y1,x0:x1])
new=cv2.imread(str(A/"fl/nuevo/0001.jpg"))
cv2.imwrite(str(A/"lane.png"),new[Y1:Y1+(Y1-Y0),683:1905])
meta={"x0":int(x0),"x1":int(x1),"y0":Y0,"y1":Y1,"liftFrame":LIFT_F,"period":per}
json.dump(meta,open(A/"clip.json","w")); open(A/"clip.js","w").write("window.CLIP="+json.dumps(meta)+";")
print("clip",x0,x1,"periodo",round(per,1))
