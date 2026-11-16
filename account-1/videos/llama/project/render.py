import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import subprocess
from common import *
name,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
mod=__import__({"desk":"desk","guy":"guy","bg":"bg"}[name])
tmp=f"out/{name}.tmp.mp4"
p=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r","30","-i","-","-c:v","libx264","-crf","17","-preset","veryfast","-pix_fmt","yuv420p","-video_track_timescale","15360",tmp],stdin=subprocess.PIPE)
for n in range(a,b):
    t=n/FPS; f=mod.frame(t)
    f=(f*VIG).astype(np.float32); g=np.random.RandomState(n).normal(0,3,(H//2,W//2)).astype(np.float32); f+=cv2.resize(g,(W,H))[:,:,None]
    p.stdin.write(np.clip(f,0,255).astype(np.uint8).tobytes())
p.stdin.close(); rc=p.wait()
if rc==0: os.rename(tmp,f"out/{name}.mp4"); print(name,"ok")
