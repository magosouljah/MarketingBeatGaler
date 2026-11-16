import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
random.seed(11)
COL={"mp3":(90,120,255),"wav":(40,200,120)}
def icon_drawn(ext,label):
    S=2; im=Image.new("RGBA",(230*S,250*S),(0,0,0,0)); d=ImageDraw.Draw(im); c=COL[ext]; x0,y0,w,h=58*S,6*S,114*S,146*S; k=34*S
    d.polygon([(x0+3*S,y0+5*S),(x0+w-k+3*S,y0+5*S),(x0+w+3*S,y0+k+5*S),(x0+w+3*S,y0+h+5*S),(x0+3*S,y0+h+5*S)],fill=(0,0,0,110))
    d.polygon([(x0,y0),(x0+w-k,y0),(x0+w,y0+k),(x0+w,y0+h),(x0,y0+h)],fill=(244,244,246,255))
    d.polygon([(x0+w-k,y0),(x0+w,y0+k),(x0+w-k,y0+k)],fill=(196,196,204,255))
    cx,cy=x0+w//2,y0+62*S
    if ext=="mp3":
        d.ellipse([cx-24*S,cy+6*S,cx-4*S,cy+24*S],fill=c+(255,)); d.ellipse([cx+8*S,cy-2*S,cx+28*S,cy+16*S],fill=c+(255,))
        d.line([(cx-6*S,cy+15*S),(cx-6*S,cy-26*S),(cx+26*S,cy-34*S),(cx+26*S,cy+7*S)],fill=c+(255,),width=5*S)
    else:
        for i,hh in enumerate((10,26,44,18,36,52,22,40,14)): d.rounded_rectangle([x0+15*S+i*10*S,cy-hh*S//2,x0+21*S+i*10*S,cy+hh*S//2],3*S,fill=c+(255,))
    d.rounded_rectangle([x0-8*S,y0+h-48*S,x0+70*S,y0+h-14*S],6*S,fill=c+(255,)); d.text((x0-1*S,y0+h-46*S),ext.upper(),font=font("Bold",25*S),fill=(255,255,255,255))
    f=font("Medium",21*S); words=label.split(" "); lines=[""]
    for wd in words:
        if d.textlength((lines[-1]+" "+wd).strip(),font=f)>214*S and lines[-1]: lines.append(wd)
        else: lines[-1]=(lines[-1]+" "+wd).strip()
    for i,ln in enumerate(lines[:2]):
        tw=d.textlength(ln,font=f); px=(230*S-tw)/2; py=(166+i*27)*S
        d.text((px+2*S,py+2*S),ln,font=f,fill=(0,0,0,200)); d.text((px,py),ln,font=f,fill=(255,255,255,255))
    a=np.array(im.resize((230,250),Image.LANCZOS)); return a[:,:,2::-1].copy(),a[:,:,3].copy()
ICO={e:cv2.imread(f"out/assets/ico_{k}.png",cv2.IMREAD_UNCHANGED) for e,k in (("flp","fl"),("als","als"))}
def icon(ext,label):
    if ext in COL: return icon_drawn(ext,label)
    S=2; src=ICO[ext]; hh=150 if ext=="flp" else 158; ww=int(src.shape[1]*hh/src.shape[0]); s=cv2.resize(src,(ww,hh),interpolation=cv2.INTER_AREA)
    base=np.zeros((250,230,4),np.uint8); x=(230-ww)//2; y=4+(158-hh)//2
    sh=np.zeros((250,230),np.uint8); sh[y+5:y+5+hh,x+3:x+3+ww]=s[:,:,3]; sh=cv2.GaussianBlur(sh,(0,0),4); base[:,:,3]=(sh*0.45).astype(np.uint8)
    al=s[:,:,3:].astype(np.float32)/255.; reg=base[y:y+hh,x:x+ww]; reg[:,:,:3]=(s[:,:,:3]*al+reg[:,:,:3]*(1-al)).astype(np.uint8); reg[:,:,3]=np.maximum(reg[:,:,3],s[:,:,3])
    im=Image.new("RGBA",(230*S,250*S),(0,0,0,0)); d=ImageDraw.Draw(im)
    f=font("Medium",21*S); words=label.split(" "); lines=[""]
    for wd in words:
        if d.textlength((lines[-1]+" "+wd).strip(),font=f)>214*S and lines[-1]: lines.append(wd)
        else: lines[-1]=(lines[-1]+" "+wd).strip()
    for i,ln in enumerate(lines[:2]):
        tw=d.textlength(ln,font=f); px=(230*S-tw)/2; py=(166+i*27)*S
        d.text((px+2*S,py+2*S),ln,font=f,fill=(0,0,0,200)); d.text((px,py),ln,font=f,fill=(255,255,255,255))
    t=np.array(im.resize((230,250),Image.LANCZOS)); ta=t[:,:,3:].astype(np.float32)/255.
    rgb=(t[:,:,2::-1]*ta+base[:,:,:3]*(1-ta)).astype(np.uint8); a=np.maximum(base[:,:,3],t[:,:,3])
    return rgb.copy(),a.copy()
NAMES=["trash beat omg.flp","goati 3.als","beat 1 (2).flp","beat final.flp","beat final FINAL.flp","beat final ahora si.flp","asdasd.flp","untitled 47.flp","trap 140 bpm.als","bounce_v3.als","master FINAL 2.als","mix test.als","idk.flp","nuevo (3).flp","drill 142 Cm.als","sin titulo.als","export_export.als","beat cliente.flp","ESTE SI.flp","no borrar.als","808 loop.als","melodia 2am.flp","copia de copia.flp","rage 150.als","plugg idea.flp","bounce 1.als","stem_kick.als","master_v9.als","aaaa.als","beat 2.flp","beat 2 OK.flp","jersey test.flp","sample chop.als","ref mix.als","vocal tag.als","beat 7 (1).flp","old old.flp","type beat.als","hi hats.als","sad piano.flp","final final.als","v2 v2.flp","loop 93.als","dark 130.flp","mixdown 3.als","demo.als","xd.flp","beat 14.flp","snare.als","lofi 80.als","nuevo.flp","test.als","perc loop.als","intro.als","beat 0.flp","backup.flp","tag.als"]
_i=0
for _k,_n in enumerate(NAMES):
    if _n.endswith('.als') and _n!='goati 3.als':
        _i+=1
        if _i%3: NAMES[_k]=_n[:-4]+('.mp3' if _i%3==1 else '.wav')
SPR={n:icon(n.rsplit(".",1)[1],n) for n in NAMES}
ICONS=[]
k=0
for r in range(8):
    for c in range(5):
        ICONS.append(dict(n=NAMES[k%len(NAMES)],x=10+c*212+random.randint(-22,22),y=335+r*196+random.randint(-20,20),rot=random.uniform(-5,5),t=-1)); k+=1
for p in range(8):
    for j in range(8):
        ICONS.append(dict(n=NAMES[k%len(NAMES)],x=random.randint(-30,880),y=random.randint(320,1640),rot=random.uniform(-17,17),t=PUL[p]+j*0.018)); k+=1
def wallpaper():
    g=np.zeros((H,W,3),np.float32); g[:]=np.array([58,30,24]); g+=np.clip(1-np.sqrt((xx-300)**2+(yy-500)**2)/1300,0,1)[:,:,None]*np.array([90,40,60]); g+=np.clip(1-np.sqrt((xx-900)**2+(yy-1600)**2)/1100,0,1)[:,:,None]*np.array([70,70,20])
    return np.clip(g,0,255).astype(np.uint8)
WP=wallpaper()
def cursor_tex():
    S=3; im=Image.new("RGBA",(60*S,80*S),(0,0,0,0)); d=ImageDraw.Draw(im); p=[(4,4),(4,60),(18,47),(28,70),(38,66),(28,43),(47,43)]
    d.polygon([(x*S,y*S) for x,y in p],fill=(255,255,255,255),outline=(0,0,0,255)); d.line([(x*S,y*S) for x,y in p+[p[0]]],fill=(0,0,0,255),width=3*S)
    a=np.array(im.resize((60,80),Image.LANCZOS)); return a[:,:,2::-1].copy(),a[:,:,3].copy()
CUR=cursor_tex(); WAY=[(random.randint(120,950),random.randint(350,1650)) for _ in range(30)]
QUERY="beat final FINAL v3.flp"
def search(t):
    im=Image.new("RGBA",(1000,250),(0,0,0,0)); d=ImageDraw.Draw(im); d.rounded_rectangle([0,0,999,128],40,fill=(24,24,28,245),outline=(90,90,100,255),width=3)
    d.ellipse([40,40,82,82],outline=(200,200,210,255),width=6); d.line([(76,78),(96,98)],fill=(200,200,210,255),width=7)
    n=int(clamp(t/1.5)*len(QUERY)); s=QUERY[:n]; f=font("Medium",46); d.text((126,34),s,font=f,fill=(255,255,255,255))
    if int(t*5)%2==0: x=126+d.textlength(s,font=f)+6; d.line([(x,30),(x,98)],fill=(255,255,255,255),width=4)
    if t>1.85:
        sh=int(math.sin(t*70)*6*(1-clamp((t-1.85)/0.4))); d.rounded_rectangle([200+sh,150,800+sh,236],43,fill=(225,45,60,250)); tx="0 resultados"; ff=font("Bold",50); d.text((500+sh-d.textlength(tx,font=ff)/2,162),tx,font=ff,fill=(255,255,255,255))
    a=np.array(im); return a[:,:,2::-1].copy(),a[:,:,3].copy()
def frame(t):
    f=WP.copy()
    for ic in ICONS:
        if t<ic["t"]: continue
        tex,al=SPR[ic["n"]]; p=(t-ic["t"])/0.14 if ic["t"]>=0 else 1
        s=eback(p,2.6) if p<1 else 1.0
        if abs(ic["rot"])>0.5 or s!=1.0:
            M=cv2.getRotationMatrix2D((115,125),ic["rot"],max(s,0.05)); tex=cv2.warpAffine(tex,M,(230,250)); al=cv2.warpAffine(al,M,(230,250))
        paste(f,tex,al,ic["x"],ic["y"])
    cv2.rectangle(f,(0,1840),(W,H),(26,22,22),-1)
    for i in range(6): cv2.rectangle(f,(60+i*110,1860),(130+i*110,1900),(70,62,60) if i else (235,150,60),-1,cv2.LINE_AA)
    sx,sa=search(t); paste(f,sx,sa,40,150)
    q=t/0.17; i=int(q); p=eo(q-i,2); a,b=WAY[i],WAY[i+1]; paste(f,CUR[0],CUR[1],lerp(a[0],b[0],p),lerp(a[1],b[1],p))
    # camera: filmed monitor feel
    pu=min(((t-p_)/0.12) for p_ in PUL if p_<=t+1e-6) if t>=PUL[0] else 1
    z=1.02+0.05*t+0.035*(1-eo(pu)); f=affine(f,z,-1.6+1.1*t+math.sin(t*23)*0.25*t/2.8,math.sin(t*31)*5*t,math.cos(t*27)*5*t)
    f[::4]=(f[::4]*0.86).astype(np.uint8)
    f=cv2.addWeighted(f,0.9,cv2.GaussianBlur(f,(0,0),18),0.28,0)
    out=clamp((t-(T_GUY-0.13))/0.13)
    if out>0: f=dblur(affine(f,1+0.1*out,0,0,1500*out*out),0,260*out)
    return f
if __name__=="__main__":
    ts=[float(x) for x in sys.argv[1:]]; cv2.imwrite("out/pv_desk.jpg",np.hstack([cv2.resize(frame(t),(540,960)) for t in ts]))
