import numpy as np, cv2, math, random
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1080,1920,30
B=[round(b-1.307,3) for b in [6.430,7.101,7.753,8.396,9.057,9.750,10.367,10.994,11.665,12.317,12.960,13.621,14.314,14.931,15.558]]; END=14.7
PUL=[0.216+0.3268*k for k in range(14)]
T_GUY=PUL[8]   # 2.83 cut to the face
T_CLICK=4.852
import os
F=os.environ.get("INTER_DIR","/usr/share/fonts/opentype/inter")+"/"
def font(w,s): return ImageFont.truetype(F+f"Inter-{w}.otf",s)
clamp=lambda x,a=0.,b=1.: max(a,min(b,x))
def eo(p,k=3): p=clamp(p); return 1-(1-p)**k
def eback(p,s=1.9): p=clamp(p)-1; return 1+p*p*((s+1)*p+s)
def lerp(a,b,p): return a+(b-a)*p
_tc={}
def text(s,w,size,col=(255,255,255),pad=6):
    k=(s,w,size,col)
    if k not in _tc:
        f=font(w,size); l,t,r,b=f.getbbox(s); im=Image.new("RGBA",(r-l+2*pad,b-t+2*pad),(0,0,0,0))
        ImageDraw.Draw(im).text((pad-l,pad-t),s,font=f,fill=col+(255,)); a=np.array(im); _tc[k]=(np.ascontiguousarray(a[:,:,2::-1]),np.ascontiguousarray(a[:,:,3]))
    return _tc[k]
def paste(dst,tex,alpha,x,y,op=1.0):
    h,w=tex.shape[:2]; x=int(round(x)); y=int(round(y)); x0,y0=max(0,x),max(0,y); x1,y1=min(dst.shape[1],x+w),min(dst.shape[0],y+h)
    if x1<=x0 or y1<=y0: return
    t=tex[y0-y:y1-y,x0-x:x1-x]; r=dst[y0:y1,x0:x1]
    if alpha is None: r[:]=t if op>=1 else cv2.addWeighted(t,op,r,1-op,0); return
    a=(alpha[y0-y:y1-y,x0-x:x1-x].astype(np.float32)*(op/255.))[:,:,None]
    r[:]=(t*a+r*(1-a)).astype(np.uint8)
def pastec(dst,ta,cx,cy,op=1.0,scale=1.0):
    t,a=ta
    if scale!=1.0:
        t=cv2.resize(t,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA if scale<1 else cv2.INTER_LINEAR); a=cv2.resize(a,(t.shape[1],t.shape[0]),interpolation=cv2.INTER_AREA if scale<1 else cv2.INTER_LINEAR)
    paste(dst,t,a,cx-t.shape[1]/2,cy-t.shape[0]/2,op)
def rot(rx,ry,rz):
    rx,ry,rz=[math.radians(v) for v in (rx,ry,rz)]
    X=np.array([[1,0,0],[0,math.cos(rx),-math.sin(rx)],[0,math.sin(rx),math.cos(rx)]]); Y=np.array([[math.cos(ry),0,math.sin(ry)],[0,1,0],[-math.sin(ry),0,math.cos(ry)]]); Z=np.array([[math.cos(rz),-math.sin(rz),0],[math.sin(rz),math.cos(rz),0],[0,0,1]])
    return X@Y@Z
def proj(P,cx,cy,f=1900.):
    z=np.maximum(f+P[:,2],60.); return np.stack([P[:,0]*f/z+cx,P[:,1]*f/z+cy],1).astype(np.float32)
def quad(dst,tex,pts,alpha=None,op=1.0):
    h,w=tex.shape[:2]; src=np.float32([[0,0],[w,0],[w,h],[0,h]])
    x0,y0=np.floor(pts.min(0)).astype(int)-1; x1,y1=np.ceil(pts.max(0)).astype(int)+1
    x0,y0=max(x0,0),max(y0,0); x1,y1=min(x1,dst.shape[1]),min(y1,dst.shape[0])
    if x1-x0<2 or y1-y0<2: return
    M=cv2.getPerspectiveTransform(src,pts-np.float32([x0,y0])); sz=(int(x1-x0),int(y1-y0))
    t=cv2.warpPerspective(tex,M,sz,flags=cv2.INTER_LINEAR)
    if alpha is None: alpha=np.full((h,w),255,np.uint8)
    a=cv2.warpPerspective(alpha,M,sz,flags=cv2.INTER_LINEAR).astype(np.float32)*(op/255.)
    r=dst[y0:y1,x0:x1]; a=a[:,:,None]; r[:]=(t*a+r*(1-a)).astype(np.uint8)
def plane(dst,tex,rx=0,ry=0,rz=0,scale=1.,cx=W/2,cy=H/2,alpha=None,op=1.,f=1900.,off=(0,0,0)):
    h,w=tex.shape[:2]; c=np.float32([[-w/2,-h/2,0],[w/2,-h/2,0],[w/2,h/2,0],[-w/2,h/2,0]])*scale
    P=c@rot(rx,ry,rz).T+np.float32(off); quad(dst,tex,proj(P,cx,cy,f),alpha,op)
def rmask(w,h,r,ss=3):
    m=Image.new("L",(w*ss,h*ss),0); ImageDraw.Draw(m).rounded_rectangle([0,0,w*ss-1,h*ss-1],r*ss,fill=255); return np.array(m.resize((w,h),Image.LANCZOS))
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
VIG=np.clip(1.08-((xx-W/2)**2/(W*0.95)**2+(yy-H/2)**2/(H*0.80)**2),0.35,1)[:,:,None]
def affine(fr,zoom=1.,ang=0.,dx=0.,dy=0.):
    M=cv2.getRotationMatrix2D((W/2,H/2),ang,zoom); M[0,2]+=dx; M[1,2]+=dy
    return cv2.warpAffine(fr,M,(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT_101)
def dblur(fr,lx,ly):
    lx,ly=int(abs(lx)),int(abs(ly))
    if lx>1: fr=cv2.blur(fr,(lx|1,1))
    if ly>1: fr=cv2.blur(fr,(1,ly|1))
    return fr
def zblur(fr,amt):
    if amt<0.01: return fr
    acc=fr.astype(np.float32)
    for k in (1,2,3): acc+=affine(fr,1+amt*k/3)
    return (acc/4).astype(np.uint8)
def rgbsplit(fr,d):
    d=int(d)
    if d<1: return fr
    o=fr.copy(); o[:,d:,2]=fr[:,:-d,2]; o[:,:-d,0]=fr[:,d:,0]; return o
# ---------- fire
rs=np.random.RandomState(3)
def ntile(n,sig):
    a=rs.rand(n,n).astype(np.float32); a=cv2.GaussianBlur(np.tile(a,(3,3)),(0,0),sig)[n:2*n,n:2*n]; return (a-a.min())/(a.max()-a.min())
NT=[ntile(256,s) for s in (22,10,4)]
FW,FH=270,480; fy,fx=np.mgrid[0:FH,0:FW].astype(np.float32)
LUT=np.zeros((256,3),np.float32)
for i in range(256):
    v=i/255.; LUT[i]=(255*clamp((v-0.72)/0.28)**1.2, 255*clamp((v-0.28)/0.5), 255*clamp(v/0.42))  # BGR
def noise(t):
    n=np.zeros((FH,FW),np.float32)
    for k,(nt,sp,sc,wg) in enumerate(zip(NT,(160,260,420),(1.,1.7,3.1),(.55,.3,.15))):
        n+=wg*cv2.remap(nt,fx*sc+17*k,fy*sc+t*sp,cv2.INTER_LINEAR,borderMode=cv2.BORDER_WRAP)
    return n
def fire(fr,grow,hole,t,ox=0.5,oy=0.62):
    """grow 0..1 fireball expanding from origin; hole 0..1 burn-away from centre revealing frame"""
    if grow<=0 or hole>=1: return fr
    n=noise(t); d=np.sqrt(((fx-ox*FW)/FW)**2+((fy-oy*FH)/FW)**2)*0.75
    v=np.clip((grow*2.6-d)/0.35+(n-0.5)*1.5*(1-grow*0.6),0,1.6)
    if grow>0.85: v+= (grow-0.85)/0.15*1.2
    if hole>0:
        dc=np.sqrt(((fx-0.5*FW)/FW)**2+((fy-0.5*FH)/FW)**2)
        v*=np.clip((dc-hole*1.9)/0.30+(n-0.5)*1.2+ (1-hole)*0.0,0,1)
        v=np.minimum(v,1.25*(1-hole)**0.35+0.2)
    v=np.clip(v,0,1); a=np.clip(v*1.7,0,1)
    col=LUT[(v*255).astype(np.uint8)]
    col=cv2.resize(col,(W,H),interpolation=cv2.INTER_CUBIC); a=cv2.resize(a,(W,H),interpolation=cv2.INTER_CUBIC)[:,:,None]
    glow=cv2.resize(cv2.GaussianBlur(col,(0,0),14),(W,H)) if False else 0
    return np.clip(fr*(1-a)+col*np.minimum(a*1.15,1)+fr*a*0.0,0,255).astype(np.uint8)
