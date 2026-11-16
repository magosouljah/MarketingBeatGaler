"""Grid-search wheel poses by silhouette IoU against reference frames (LOCAL QA).

    FIT_REF_FRAMES=<Reference Analysis frames dir of the reference> FIT_TIMES=1.9,2.2,2.6 \
    [FIT_LABBG=12,12,12] [FIT_TEXTBOX=1] python tools/fit_silhouette.py GRID.json OUT.json
GRID.json: list of RIG overrides (objects merged over RIG). Reference frame
numbers are original-clock frames (Instagram encode: file frame N = original N).
The reference ground is assumed #f3f3f3; FIT_LABBG gives the lab's ground.
"""
import functools,http.server,threading,io,json,sys,itertools,os
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright
from pathlib import Path
ROOT=str(Path(__file__).resolve().parents[1]/'hyperframes')
F=os.environ['FIT_REF_FRAMES']
import os
TIMES=[float(x) for x in os.environ.get("FIT_TIMES","1.9,2.2,2.6").split(",")]
def mask(im,bg=(243,243,243)):
    a=np.asarray(im.convert('RGB').resize((90,160),Image.BILINEAR)).astype(float)
    m=np.linalg.norm(a-np.array(bg),axis=2)>30
    if os.environ.get("FIT_TEXTBOX","1")=="1": m[59:76,22:72]=False  # reference text box (0.37-0.47 H, 0.25-0.8 W) excluded
    m[:16,:]=False if os.environ.get("FIT_TOPBAND")=="1" else m[:16,:]
    return m
refm=[mask(Image.open(f'{F}/{round(t*30):06d}.png')) for t in TIMES]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
h=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory=ROOT));threading.Thread(target=h.serve_forever,daemon=True).start()
grid=json.loads(open(sys.argv[1]).read())
res=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=os.environ.get('CHROME','/usr/bin/google-chrome'),args=['--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    pg=b.new_page(viewport={'width':720,'height':1280});pg.goto(f'http://127.0.0.1:{h.server_address[1]}/index.html');pg.wait_for_function('window.__lab!==undefined',timeout=60000)
    pg.add_style_tag(content=".word,#brand,#endcard{display:none!important}")
    pg.evaluate("async()=>{window.__m=await import('./src/wheel.js');}")
    for c in grid:
        ious=[]
        pg.evaluate("async (c)=>{const m=window.__m;const rig=Object.assign({},m.RIG,c);const cv=document.getElementById('stage');const f=cv.cloneNode();f.id='stage';cv.replaceWith(f);window.__x=m.createWheel(f,rig);await window.__x.ready;}",c)
        for t,rm in zip(TIMES,refm):
            pg.evaluate(f"window.__x.render({t})")
            om=mask(Image.open(io.BytesIO(pg.screenshot())),tuple(int(x) for x in os.environ.get('FIT_LABBG','243,243,243').split(',')))
            ious.append((om&rm).sum()/max((om|rm).sum(),1))
        res.append((float(np.mean(ious)),c))
    b.close()
res.sort(key=lambda r:-r[0])
json.dump(res,open(sys.argv[2],'w'))
for s,c in res[:6]: print(round(s,3),json.dumps({k:v for k,v in c.items() if k!='spread'}))
