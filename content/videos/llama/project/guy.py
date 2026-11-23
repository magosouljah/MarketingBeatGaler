import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
CLIP="inputs/guy.mp4"; FR=None
if os.path.exists(CLIP):
    cap=cv2.VideoCapture(CLIP); FR=[]
    while True:
        ok,f=cap.read()
        if not ok: break
        FR.append(f)
def room():
    g=np.zeros((H,W,3),np.float32); g[:]=(20,12,14)
    g+=np.clip(1-np.sqrt((xx-150)**2+(yy-500)**2)/700,0,1)[:,:,None]**2*np.array([150,30,110]); g+=np.clip(1-np.sqrt((xx-980)**2+(yy-900)**2)/600,0,1)[:,:,None]**2*np.array([120,40,20])
    for x in (90,860): cv2.rectangle(g,(x,980),(x+170,1300),(34,26,28),-1); cv2.circle(g,(x+85,1090),48,(50,40,44),-1); cv2.circle(g,(x+85,1220),26,(50,40,44),-1)
    return cv2.GaussianBlur(np.clip(g,0,255),(0,0),16)
ROOM=room(); GL=np.clip((yy-500)/900,0,1)
def standin(t):
    u=t-T_GUY; f=ROOM.copy(); m=np.zeros((H,W),np.uint8)
    fr=clamp(u/0.3)*(1-clamp((u-1.7)/0.3)); sx=math.sin(u*10)*60*fr; dy=110*eo(u/0.5)*(1-eo((u-1.75)/0.3))
    hx,hy=int(540+sx),int(760+dy)
    cv2.ellipse(m,(540,1700),(520,560),0,180,360,255,-1,cv2.LINE_AA); cv2.rectangle(m,(20,1690),(1060,H),255,-1)
    cv2.rectangle(m,(hx-80,hy+150),(hx+80,hy+330),255,-1); cv2.ellipse(m,(hx,hy),(205,255),0,0,360,255,-1,cv2.LINE_AA); cv2.ellipse(m,(hx,hy-150),(225,150),0,180,360,255,-1,cv2.LINE_AA)
    cv2.ellipse(m,(hx,hy-60),(250,290),0,200,340,255,26,cv2.LINE_AA)
    rp=eback((u-2.25)/0.45,1.2)                          # lighter + perfume come up
    LX,LY=int(330),int(lerp(2100,1230,rp)); PX,PY=int(760),int(lerp(2150,1200,rp))
    for (qx,qy) in ((LX,LY),(PX,PY)): cv2.ellipse(m,(qx,qy+150),(105,140),0,0,360,255,-1,cv2.LINE_AA); cv2.line(m,(qx,qy+200),(qx+(-160 if qx<540 else 160),1950),255,150,cv2.LINE_AA)
    body=np.zeros((H,W,3),np.float32); body[:]=(26,20,22); body+=GL[:,:,None]*np.array([150,105,70])*0.55
    edge=cv2.GaussianBlur(m,(0,0),10).astype(np.float32)/255.; rim=np.clip((edge-cv2.GaussianBlur(m,(0,0),34).astype(np.float32)/255.)*3,0,1)[:,:,None]
    body+=rim*np.array([230,170,120])*0.7
    a=cv2.GaussianBlur(m,(0,0),2.5).astype(np.float32)[:,:,None]/255.; f=f*(1-a)+body*a
    f=np.clip(f,0,255).astype(np.uint8)
    if rp>0.05:
        cv2.rectangle(f,(LX-34,LY-70),(LX+34,LY+60),(60,150,60),-1,cv2.LINE_AA); cv2.rectangle(f,(LX-34,LY-98),(LX+34,LY-70),(190,190,195),-1,cv2.LINE_AA)
        ov=f.copy(); cv2.rectangle(ov,(PX-80,PY-70),(PX+80,PY+95),(230,190,60),-1,cv2.LINE_AA); cv2.rectangle(ov,(PX-28,PY-125),(PX+28,PY-70),(215,215,220),-1,cv2.LINE_AA); f=cv2.addWeighted(ov,0.85,f,0.15,0)
        cv2.rectangle(f,(PX-60,PY-50),(PX-36,PY+75),(255,235,170),-1,cv2.LINE_AA)
    if t>=T_CLICK:
        fl=np.zeros((H,W,3),np.float32); k=1+0.15*math.sin(t*90); cv2.ellipse(fl,(LX,LY-165),(int(30*k),int(72*k)),0,0,360,(60,170,255),-1,cv2.LINE_AA); cv2.ellipse(fl,(LX,LY-145),(15,40),0,0,360,(200,245,255),-1,cv2.LINE_AA)
        f=np.clip(f.astype(np.float32)+cv2.GaussianBlur(fl,(0,0),6)+cv2.GaussianBlur(fl,(0,0),90)*2.2,0,255).astype(np.uint8)
    f=cv2.GaussianBlur(f,(0,0),1.6); return f,(LX/W,(LY-165)/H)
KEYS=[(T_GUY,0.35),(PUL[11],3.0),(PUL[13],4.25),(T_CLICK,5.2),(B[0],6.0)]
def clipframe(t):
    kt=[k[0] for k in KEYS]; kc=[k[1] for k in KEYS]
    c0=np.interp(t,kt,kc)*24; c1=np.interp(t+1/FPS,kt,kc)*24; n=max(1,int(np.ceil((c1-c0)*2))); acc=0
    for j in range(n):
        x=min(len(FR)-1.001,c0+(c1-c0)*j/n); i=int(x); w=x-i; acc=acc+FR[i][0:640,60:420].astype(np.float32)*(1-w)+FR[i+1][0:640,60:420].astype(np.float32)*w
    f=cv2.resize(np.clip(acc/n,0,255).astype(np.uint8),(W,H),interpolation=cv2.INTER_LANCZOS4)
    f=cv2.addWeighted(f,1.6,cv2.GaussianBlur(f,(0,0),4),-0.6,0); f=cv2.convertScaleAbs(f,alpha=1.12,beta=4)
    return f,(0.53,0.66)
def frame(t):
    f,(ox,oy)=clipframe(t) if FR else standin(t)
    u=t-T_GUY; q=1-eo(u/0.16,2); late=clamp((t-T_CLICK)/(B[0]-T_CLICK))
    z=1.03+0.03*u+0.16*late*late+(0.06*(1-eo((t-PUL[11])/0.15)) if t>=PUL[11] else 0); sh=2+16*late
    f=affine(f,z,math.sin(t*17)*0.3,math.sin(t*41)*sh,-1500*q+math.cos(t*37)*sh)
    if q>0.01: f=dblur(f,0,260*q)
    if abs(t-T_CLICK)<0.034: f=cv2.convertScaleAbs(f,alpha=1.25,beta=20)
    g=clamp((t-(T_CLICK+(0.10 if FR else 0.03)))/(B[0]-0.035-(T_CLICK+(0.10 if FR else 0.03))))
    if g>0: f=fire(f,g**1.4,0,t,ox,oy)
    return f
if __name__=="__main__":
    ts=[float(x) for x in sys.argv[1:]]; cv2.imwrite("out/pv_guy.jpg",np.hstack([cv2.resize(frame(t),(360,640)) for t in ts]))
