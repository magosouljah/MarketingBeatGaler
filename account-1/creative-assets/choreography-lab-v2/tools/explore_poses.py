"""Render RIG overrides side by side at one time (LOCAL QA).

    python tools/explore_poses.py CANDIDATES.json T OUT.jpg
"""
import functools,http.server,threading,io,json,sys,os
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright
from pathlib import Path
ROOT=str(Path(__file__).resolve().parents[1]/'hyperframes')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
h=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory=ROOT));threading.Thread(target=h.serve_forever,daemon=True).start()
cands=json.loads(open(sys.argv[1]).read()); t=float(sys.argv[2]); out=sys.argv[3]
ims=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=os.environ.get('CHROME','/usr/bin/google-chrome'),args=['--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    pg=b.new_page(viewport={'width':720,'height':1280});pg.goto(f'http://127.0.0.1:{h.server_address[1]}/index.html');pg.wait_for_function('window.__lab!==undefined',timeout=60000)
    pg.add_style_tag(content=".word,#brand,#endcard{display:none!important}")
    for c in cands:
        pg.evaluate("""async ([c,t]) => { const m = await import('./src/wheel.js'); const rig = Object.assign({}, m.RIG, c);
          const cv = document.getElementById('stage'); const fresh = cv.cloneNode(); cv.replaceWith(fresh);
          const lab = m.createWheel(fresh, rig); await lab.ready; lab.render(t); }""",[c,t])
        ims.append(Image.open(io.BytesIO(pg.screenshot())).convert('RGB').resize((160,284)))
    b.close()
S=Image.new('RGB',(len(ims)*164,300),'white');d=ImageDraw.Draw(S)
for i,im in enumerate(ims): S.paste(im,(i*164,16)); d.text((i*164+2,2),str(i),fill='black')
S.save(out)
