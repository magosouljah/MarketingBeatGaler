"""Prepara todo lo que project/ necesita, a partir de inputs/ (ver inputs/README.md).

Ejecutar desde content/videos/llama/:   python tools/prepare.py
Escribe en out/assets/ (ignorado por Git): portadas, tarjetas, muro, mosaico, logotipo,
iconos recortados y out/audio.wav (la pista de la referencia extendida a 14.7 s).
"""
import os, subprocess, wave, random
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
os.makedirs("out/assets", exist_ok=True)
F=os.environ.get("INTER_DIR","/usr/share/fonts/opentype/inter")+"/"

# ---------------------------------------------------------------- 1. texturas de BeatGaler
# Portadas recortadas de la captura de la Gallery; nombres, tags y BPM re-tipografiados
# (el texto de 8 px de la captura no aguanta ampliarse 3x).
def font(w,s): return ImageFont.truetype(F+f"Inter-{w}.otf",s)
g=cv2.imread("inputs/gallery.jpg"); l=cv2.imread("inputs/landing.jpg")
assert g is not None and l is not None, "faltan inputs/gallery.jpg o inputs/landing.jpg"
assert g.shape[:2]==(874,1600) and l.shape[:2]==(769,1600), "las coordenadas de recorte son para capturas de 1600x874 (gallery) y 1600x769 (landing)"
xs=[273,425,578,730,882,1035,1187]
META=[("Vanta",["Ambient","Trap","Dark","Melodic","Spacey"],"D minor · 98 BPM"),("Lumen",["Electronic","Synthwave","Club","Pop"],"F minor · 116 BPM"),("Kairo",["Trap","Rage","Drill","Aggressive","Memphis"],"G minor · 144 BPM"),("Sable",["Electronic","House","Club","Bounce"],"A minor · 132 BPM"),("Echo",["Ambient","LoFi","Chill","Piano"],"E minor · 90 BPM"),
("Bloom",["Electronic","Melodic","Soul","RnB"],"G major · 105 BPM"),("Quartz",["Trap","Drill","Detroit","West Coast"],"C# minor · 142 BPM"),("Orbit",["Electronic","House","Synthwave","Spacey"],"F# minor · 126 BPM"),("Haze",["Ambient","Sampled","Soul","Chill"],"A major · 84 BPM"),("Pulse",["Trap","Aggressive","Club","Memphis","Bounce"],"D minor · 152 BPM"),("Frost",["Ambient","Cinematic","Piano","Sad"],"E major · 100 BPM"),("Nova",["Electronic","Hyperpop","Pop","Rage"],"C minor · 136 BPM"),
("Halo",["Ambient","Latin","Guitar","Soul"],"D major · 112 BPM"),("Prism",["Ambient","Trap","Experimental","Sampled","Dark"],"F minor · 124 BPM"),("Abyss",["Trap","Drill","Jersey","Aggressive"],"B minor · 130 BPM"),("Veil",["Ambient","LoFi","Piano","Chill"],"G major · 80 BPM"),("Flux",["Electronic","Funk","Club","House"],"C major · 120 BPM"),("Crave",["Trap","Detroit","West Coast","BoomBap"],"A minor · 150 BPM"),("Serein",["Ambient","Afro","Latin","Vocal","Experimental"],"E minor · 92 BPM")]
def up(im,s):
    im=cv2.resize(im,(s,s),interpolation=cv2.INTER_LANCZOS4)
    b=cv2.GaussianBlur(im,(0,0),2.2); return cv2.addWeighted(im,1.5,b,-0.5,0)
def rmask(w,h,r,ss=3):
    m=Image.new("L",(w*ss,h*ss),0); ImageDraw.Draw(m).rounded_rectangle([0,0,w*ss-1,h*ss-1],r*ss,fill=255)
    return np.array(m.resize((w,h),Image.LANCZOS))
TS=360
tiles=[]
for i in range(5): tiles.append(up(g[101:206, xs[i]+15:xs[i]+120],TS))
for y in (316,558):
    for x in xs: tiles.append(up(g[y+2:y+132,x+2:x+132],TS))
np.save("out/assets/tiles.npy",np.array(tiles))
BG=(15,14,14)
def card(i,W=420,H=640):
    im=Image.new("RGB",(W,H),BG[::-1]); d=ImageDraw.Draw(im)
    t=Image.fromarray(tiles[i][:,:,::-1]); im.paste(t,(30,24),Image.fromarray(rmask(TS,TS,18)))
    d.text((30,TS+44),META[i][0],font=font("Bold",30),fill=(245,245,245))
    x,y=30,TS+96; f=font("Medium",19)
    for tg in META[i][1]:
        w=int(d.textlength(tg,font=f))+30
        if x+w>W-20: x=30; y+=48
        d.rounded_rectangle([x,y,x+w,y+36],18,outline=(70,70,74),width=2); d.text((x+15,y+6),tg,font=f,fill=(200,200,205)); x+=w+10
    d.text((30,y+54),META[i][2],font=font("Regular",20),fill=(140,140,146))
    return np.array(im)[:,:,::-1]
cards=[card(i) for i in range(19)]
np.save("out/assets/cards.npy",np.array(cards))
random.seed(7); order=list(range(19)); 
cols,rows=6,6; wall=np.zeros((rows*640,cols*420,3),np.uint8)
seq=[]
while len(seq)<cols*rows:
    random.shuffle(order); seq+=order
for k in range(cols*rows):
    r,c=divmod(k,cols); wall[r*640:(r+1)*640,c*420:(c+1)*420]=cards[seq[k]]
cv2.imwrite("out/assets/wall.png",wall)
# cover-only mosaic (tileable)
mos=np.zeros((6*TS,6*TS,3),np.uint8); mos[:]=BG
m=rmask(TS-24,TS-24,20)[:,:,None]/255.
for k in range(36):
    r,c=divmod(k,6); t=cv2.resize(tiles[seq[(k*7)%len(seq)]],(TS-24,TS-24),interpolation=cv2.INTER_AREA)
    reg=mos[r*TS+12:(r+1)*TS-12,c*TS+12:(c+1)*TS-12]; reg[:]=(t*m+reg*(1-m)).astype(np.uint8)
cv2.imwrite("out/assets/mosaic.png",mos)
# wordmark
wm=cv2.cvtColor(l[312:394,668:958],cv2.COLOR_BGR2GRAY).astype(np.float32)
wm=cv2.resize(wm,None,fx=5,fy=5,interpolation=cv2.INTER_CUBIC); wm=cv2.GaussianBlur(wm,(0,0),2.5)
wm=np.clip((wm-118)/22+0.5,0,1); 
cv2.imwrite("out/assets/wordmark.png",(wm*255).astype(np.uint8))

# ---------------------------------------------------------------- 2. iconos de archivo
# flp.png: icono redondo sobre blanco -> mascara circular (el relleno por inundacion se mete al icono).
# als.png: hoja oscura sobre blanco  -> inundacion desde las esquinas + componente mas grande (quita el nombre).
im=cv2.imread("inputs/flp.png"); assert im is not None, "falta inputs/flp.png"
gm=(im.max(2)<225); cols=np.where(gm.sum(0)>0)[0]; rows=np.where(gm.sum(1)>0)[0]
x0,x1,y0=cols[0],cols[-1],rows[0]; d=x1-x0; y1=y0+d; S=4
al=np.zeros((im.shape[0]*S,im.shape[1]*S),np.uint8); cv2.circle(al,(int((x0+x1)/2*S+S/2),int((y0+y1)/2*S+S/2)),int((d/2-1)*S),255,-1,cv2.LINE_AA)
al=cv2.resize(al,(im.shape[1],im.shape[0]),interpolation=cv2.INTER_AREA)
cv2.imwrite("out/assets/ico_fl.png",np.dstack([im,al])[y0:y1+1,x0:x1+1])
im=cv2.imread("inputs/als.png"); assert im is not None, "falta inputs/als.png"
h,w=im.shape[:2]; bgm=np.zeros((h,w),np.uint8)
for s in ((0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0)):
    mk=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(im.copy(),mk,s,(255,0,255),(12,12,12),(12,12,12),flags=8|cv2.FLOODFILL_MASK_ONLY|(255<<8)); bgm|=mk[1:-1,1:-1]
n,lab,st,_=cv2.connectedComponentsWithStats(255-bgm); k=1+np.argmax(st[1:,cv2.CC_STAT_AREA])
al=cv2.GaussianBlur((lab==k).astype(np.uint8)*255,(0,0),0.8); x,y,ww,hh=st[k,:4]
cv2.imwrite("out/assets/ico_als.png",np.dstack([im,al])[y:y+hh,x:x+ww])

# ---------------------------------------------------------------- 3. audio
# La referencia dura 7.5 s. Tiempos medidos en ESA grabacion (transientes, no BPM):
#   pulsos del buildup 0.216 .. 1.842 (cada 0.327 s) | golpecito 2.238 | drop 2.509
#   golpes 2.509 3.180 3.832 4.475 5.136 5.829 6.446 7.073
# Montaje: [0, 1.523] + 2 x [0.216, 1.523] + [1.523, 7.073] + [2.509, fin]  ->  14.7 s
# Con otra pista hay que volver a medir (shared/editing/find_hits.py) y cambiar B, PUL y T_CLICK en project/common.py.
subprocess.run(["ffmpeg","-v","error","-y","-i","inputs/reference.mov","-vn","-ar","44100","-ac","2","out/assets/orig.wav"],check=True)
w=wave.open("out/assets/orig.wav"); sr=w.getframerate(); y=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32).reshape(-1,2)/32768
pre=0.006
def seg(a,b): return y[int((a-pre)*sr) if a>0 else 0:int((b-pre)*sr) if b else len(y)]
parts=[seg(0,1.523)]+[seg(0.216,1.523)]*2+[seg(1.523,7.073),seg(2.509,None)]
xf=int(0.005*sr); out=parts[0].copy()
for p in parts[1:]:
    r=np.linspace(0,1,xf)[:,None]; out[-xf:]=out[-xf:]*(1-r)+p[:xf]*r; out=np.vstack([out,p[xf:]])
n=int(14.7*sr); out=np.vstack([out,np.zeros((max(0,n-len(out)),2),np.float32)])[:n]
f=int(0.35*sr); out[-f:]*=np.linspace(1,0,f)[:,None]**1.5
ww=wave.open("out/audio.wav","wb"); ww.setnchannels(2); ww.setsampwidth(2); ww.setframerate(sr); ww.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes())
print("prepare ok")
