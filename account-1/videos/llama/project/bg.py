import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
tiles=np.load("out/assets/tiles.npy"); cards=np.load("out/assets/cards.npy"); wall=cv2.imread("out/assets/wall.png"); mos=cv2.imread("out/assets/mosaic.png"); WM=cv2.imread("out/assets/wordmark.png",0)
TS=360; TM=rmask(TS,TS,22); CM=rmask(420,640,26)
BGC=np.array([15,14,14],np.float32)
d=np.sqrt((xx-W/2)**2+(yy-H/2)**2)/H
BASE=(BGC+np.clip(1-d*2.2,0,1)[:,:,None]**2*np.array([34,26,24],np.float32)).astype(np.uint8)
def bg(): return BASE.copy()
def wordmark(dst,cx,cy,width,op=1.,**pl):
    s=width/WM.shape[1]; a=cv2.resize(WM,None,fx=s,fy=s,interpolation=cv2.INTER_AREA); t=np.full(a.shape+(3,),255,np.uint8)
    if pl: plane(dst,t,cx=cx,cy=cy,alpha=a,op=op,**pl)
    else: paste(dst,t,a,cx-a.shape[1]/2,cy-a.shape[0]/2,op)
def ring(dst,ang,rx,ry,rz,scale=1.,cx=W/2,cy=H/2,Rx=455,Ry=640,ts=250,op=1.,n=19):
    R=rot(rx,ry,rz); items=[]
    for i in range(n):
        a=ang+i*2*math.pi/n; c=np.array([Rx*math.cos(a),Ry*math.sin(a),0.]); tw=math.degrees(math.sin(a*2+i)*0.22)
        h=ts/2; cs=np.float32([[-h,-h,0],[h,-h,0],[h,h,0],[-h,h,0]])@rot(0,0,tw).T+c
        P=(cs*scale)@R.T; items.append((P[:,2].mean(),i,P))
    for z,i,P in sorted(items,key=lambda v:-v[0]):
        sh=clamp(1.05-(z+500)/2600,0.45,1.)
        quad(dst,tiles[i],proj(P,cx,cy),TM,op*sh)
def scroll(tex,dx,dy): return np.roll(np.roll(tex,int(dy)%tex.shape[0],0),int(dx)%tex.shape[1],1)
GEN=["BoomBap","Ambient","Trap","Electronic","Dark","Melodic","Rage","Drill","House","Jersey","Pluggnb","LoFi","RnB","Synthwave","Sad","Vocal"]
def _rows():
    out=[]
    for r in range(11):
        im=Image.new("RGB",(5200,190),(15,14,14)); dr=ImageDraw.Draw(im); x=0; f=font("Bold",128); k=r*3
        while x<5200:
            g=GEN[k%16]; w=dr.textlength(g,font=f); hi=(k%5==2)
            if hi: dr.rounded_rectangle([x-26,12,x+w+26,178],83,fill=(245,245,245))
            dr.text((x,22),g,font=f,fill=(15,14,14) if hi else ((235,235,235) if r%2==0 else (120,120,126))); x+=w+90; k+=1
        out.append(np.array(im)[:,:,::-1].copy())
    return out
ROWS=_rows()
def player_tex():
    Wp,Hp=980,190; im=Image.new("RGBA",(Wp,Hp),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,Wp-1,Hp-1],60,fill=(30,30,32,255),outline=(60,60,64,255),width=2)
    d.polygon([(70,62),(70,128),(124,95)],fill=(245,245,245,255))
    im.paste(Image.fromarray(cv2.resize(tiles[0],(110,110))[:,:,::-1]),(170,40),Image.fromarray(rmask(110,110,16)))
    d.text((306,44),"Vanta",font=font("Bold",40),fill=(245,245,245,255)); d.text((306,100),"D minor  •  98 BPM",font=font("Regular",28),fill=(165,165,170,255))
    for i,hh in enumerate((30,56,40,66,34)): d.rounded_rectangle([820+i*22,95-hh/2,832+i*22,95+hh/2],6,fill=(245,245,245,255))
    a=np.array(im); return a[:,:,2::-1].copy(),a[:,:,3].copy()
PLAYER=player_tex()
def button_tex():
    Wb,Hb=560,150; im=Image.new("RGBA",(Wb,Hb),(0,0,0,0)); d=ImageDraw.Draw(im); d.rounded_rectangle([0,0,Wb-1,Hb-1],75,fill=(245,245,245,255))
    d.text((70,46),"Create ur Galer",font=font("Bold",46),fill=(15,14,14,255)); d.line([(440,76),(492,76)],fill=(15,14,14,255),width=5); d.line([(474,58),(492,76),(474,94)],fill=(15,14,14,255),width=5,joint="curve")
    a=np.array(im); return a[:,:,2::-1].copy(),a[:,:,3].copy()
BTN=button_tex()
def circ(n): 
    m=np.zeros((n,n),np.uint8); cv2.circle(m,(n//2,n//2),n//2-2,255,-1,cv2.LINE_AA); return m

def s0(u,tl):   # ring hero
    f=bg(); e=eo(tl/0.5); ring(f,tl*0.5,lerp(34,16,e),lerp(-30,-14,e),lerp(-8,0,e),scale=lerp(1.25,1.0,e))
    wordmark(f,W/2,H/2-10,640); pastec(f,text("Unlimited cloud storage for your beats.","Regular",34,(170,170,176)),W/2,H/2+95); return f
def s1(u,tl):   # ring tilted close
    f=bg(); ring(f,1+tl*1.6,58,8,24+tl*10,scale=1.75+tl*0.15,cy=H/2+60); wordmark(f,W/2,H/2,930,rx=0,ry=-22,rz=-7,scale=1+tl*0.05); return f
def s2(u,tl):   # wall isometric
    f=bg(); plane(f,scroll(wall,-tl*260,-tl*520-200),rx=46,rz=-32,scale=0.95+tl*0.05,cy=H/2-40,f=2400); return f
def s3(u,tl):   # wall side
    f=bg(); plane(f,scroll(wall,-tl*700,0)[:2560],ry=-56,rx=4,scale=1.25,cx=W/2+120,f=1500); return f
def s4(u,tl):   # big card flip
    f=cv2.GaussianBlur(cv2.resize(scroll(mos,0,-tl*120)[:1920,:1080],(270,480)),(0,0),9); f=(cv2.resize(f,(W,H))*0.38).astype(np.uint8)
    e=eback(tl/0.32); plane(f,cards[0],ry=lerp(82,-9,e),rx=5,rz=lerp(-10,2,e),scale=1.95+tl*0.08,alpha=CM,cy=H/2-20); return f
def s5(u,tl):   # slanted strips
    f=bg(); big=np.zeros((2400,1440,3),np.uint8); big[:]=(15,14,14)
    for i in range(3):
        col=scroll(mos,-i*720-360*(i%2),(1 if i%2==0 else -1)*tl*900+i*300); col=cv2.resize(col[:,:360],(440,2640),interpolation=cv2.INTER_LINEAR)[:2400]
        big[:,i*480+20:i*480+460]=col
    e=eo(tl/0.25); return affine(cv2.resize(big,(W,1800))[:1800].copy() if False else cv2.copyMakeBorder(cv2.resize(big,(1296,2160)),0,0,0,0,cv2.BORDER_CONSTANT)[120:2040,108:1188],1.22,lerp(-24,-11,e))
RM820=rmask(820,820,44); C900=circ(900); C240=circ(240)
def s6(u,tl):   # circles / vinyl
    f=bg(); e=eback(tl/0.3)
    for k in range(8):
        a=tl*1.4+k*math.pi/4; i=[3,1,5,9,14,16,11,4][k]; r=lerp(300,690,e); pastec(f,(cv2.resize(tiles[i],(240,240),interpolation=cv2.INTER_AREA),C240),W/2+r*math.cos(a),H/2+r*1.08*math.sin(a))
    t=cv2.resize(tiles[8],(900,900),interpolation=cv2.INTER_CUBIC); M=cv2.getRotationMatrix2D((450,450),-tl*200,1.12); t=cv2.warpAffine(t,M,(900,900),borderMode=cv2.BORDER_REFLECT)
    cv2.circle(t,(450,450),448,(245,245,245),6,cv2.LINE_AA); cv2.circle(t,(450,450),62,(15,14,14),-1,cv2.LINE_AA); cv2.circle(t,(450,450),62,(245,245,245),4,cv2.LINE_AA)
    pastec(f,(t,C900),W/2,H/2,scale=lerp(0.55,0.86,e)); return f
def s7(u,tl):   # genre marquee
    cv=np.zeros((2400,2600,3),np.uint8); cv[:]=(15,14,14)
    for r in range(11): cv[60+r*210:250+r*210]=scroll(ROWS[r],(-1 if r%2 else 1)*tl*620-r*370-900,0)[:,:2600]
    f=bg(); plane(f,cv,rx=26,ry=-14,rz=-13,scale=1.0+tl*0.06,f=2200); return f
def s8(u,tl):   # floor crawl
    f=bg(); plane(f,scroll(wall,0,tl*1100)[:2400],rx=-68,scale=0.9,cy=H/2-100,f=1500)
    g=np.clip((yy-640)/420,0,1)[:,:,None]; f=(f*g+BASE*(1-g)).astype(np.uint8); wordmark(f,W/2,430,560); return f
def s9(u,tl):   # fan of cards
    f=bg(); e=eback(tl/0.36,1.4); idx=[15,3,8,0,4]; px,py=W/2,2740
    for k in (0,4,1,3,2):
        a=math.radians((k-2)*10.5*e+tl*2); s=1.42; c=np.float32([[-210,-640-880],[210,-640-880],[210,-880],[-210,-880]])*np.float32([s,1])
        c[:,1]=np.float32([-1150-640*s,-1150-640*s,-1150,-1150]); R2=np.float32([[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]])
        quad(f,cards[idx[k]],(c@R2.T+np.float32([px,py])).astype(np.float32),CM)
    return f
def s10(u,tl):  # player
    f=bg(); e=eo(tl/0.3); t=cv2.resize(tiles[0],(820,820),interpolation=cv2.INTER_CUBIC)
    plane(f,t,ry=lerp(-48,-20,e),rx=8,rz=lerp(6,-3,e),scale=1.12+tl*0.05,alpha=RM820,cy=800)
    p=PLAYER[0].copy(); x1=306+int(470*clamp(0.15+tl*0.5)); cv2.line(p,(306,158),(776,158),(80,80,84),5,cv2.LINE_AA); cv2.line(p,(306,158),(x1,158),(245,245,245),5,cv2.LINE_AA)
    paste(f,p,PLAYER[1],50,lerp(1700,1370,eback(tl/0.3))); return f
def s11(u,tl):  # diamonds
    f=bg(); m=scroll(mos,-tl*300,-tl*300); big=np.tile(m,(1,1,1)); return affine(cv2.resize(big,(2160,2160))[120:2040,540:1620].copy(),1.5+tl*0.25,45+tl*14)
def s13(u,tl):  # final lockup
    f=bg(); b1=B[13]-B[12]; b2=B[14]-B[12]
    if tl<b1: rx,ry,rz,sc=48,-20,14,1.2
    elif tl<b2: rx,ry,rz,sc=-30,26,-8,1.1
    else: rx,ry,rz,sc=0,0,0,1.0
    seg=tl if tl<b1 else (tl-b1 if tl<b2 else tl-b2); pu=1+0.07*(1-eo(seg/0.25))
    ring(f,0.4+tl*0.35,rx,ry,rz,scale=sc*pu,op=0.92)
    wordmark(f,W/2,H/2-70,int(680*pu)); pastec(f,text("Unlimited cloud storage for your beats.","Regular",34,(175,175,180)),W/2,H/2+38)
    if tl>=b1: pastec(f,BTN,W/2,H/2+190,scale=0.8*(1+0.10*(1-eo((tl-b1)/0.25) if tl<b2 else 0.10*(1-eo((tl-b2)/0.25)))))
    return f
SHOTS=[(s0,'zoom'),(s1,'spin'),(s2,'whipL'),(s3,'whipR'),(s4,'zoom'),(s5,'whipU'),(s6,'spin'),(s7,'whipL'),(s8,'whipD'),(s9,'zoom'),(s10,'whipR'),(s11,'spin')]
def frame(t):
    i=max(k for k in range(len(B)) if t>=B[k]-1e-6); i=min(i,12); s=B[i]; e=B[i+1] if i<12 else END; tl=t-s
    fn,ty=SHOTS[i] if i<12 else (s13,'zoom'); f=fn((t-s)/(e-s),tl)
    if i==12:
        b1=B[13]-B[12]; b2=B[14]-B[12]; tl=tl if tl<b1 else (tl-b1 if tl<b2 else tl-b2); e=min(e,END) ; ty=['zoom','spin','zoom'][0 if t<B[13] else (1 if t<B[14] else 2)]; out=0
    else: out=clamp((t-(e-0.07))/0.07)
    q=1-eo(tl/0.2); z=1+0.20*q+0.10*out*out; ang=dx=dy=0
    if ty=='spin': ang=14*q
    if ty=='whipL': dx=520*q
    if ty=='whipR': dx=-520*q
    if ty=='whipU': dy=520*q
    if ty=='whipD': dy=-520*q
    if q>0.002 or out>0:
        f=affine(f,z,ang,dx,dy); f=dblur(f,abs(dx)*0.35,abs(dy)*0.35)
        if ty in('zoom','spin') or out>0: f=zblur(f,0.10*q+0.07*out)
        f=rgbsplit(f,16*q+6*out); f=cv2.convertScaleAbs(f,alpha=1+0.5*q,beta=45*q*q)
    # fire burn-away after the explosion
    if t<B[0]+0.75: f=fire(f,1.0,((t-B[0])/0.75)**1.3 if t>B[0]+0.035 else 0.0,t)
    return f
def finish(f,t,seed):
    f=(f*VIG).astype(np.float32); g=np.random.RandomState(seed).normal(0,5.5,(H//2,W//2,1)).astype(np.float32); f+=cv2.resize(g,(W,H))[:,:,None]
    return np.clip(f,0,255).astype(np.uint8)
if __name__=="__main__":
    ts=[float(x) for x in sys.argv[1:]]
    ims=[cv2.resize(finish(frame(t),t,1),(360,640)) for t in ts]; cv2.imwrite("out/pv_bg.jpg",np.hstack(ims))
