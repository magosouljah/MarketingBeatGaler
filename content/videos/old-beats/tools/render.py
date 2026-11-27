#!/usr/bin/env python3
"""Filma project/index.html con Chrome (Playwright), como content/videos/fuck pero capturando la pagina entera.

    render.py frames <dir> t1 t2 ...        frames sueltos (JPEG) en segundos de video
    render.py seg <salida.mp4> t_ini t_fin  un tramo a 30 fps

Sirve la raiz de content/videos por HTTP (la rueda se importa como modulo desde ../wheel). CHROME = ruta del navegador."""
import functools, http.server, os, subprocess, sys, threading
from pathlib import Path
from playwright.sync_api import sync_playwright
FPS=30; HERE=Path(__file__).resolve().parent.parent; ROOT=HERE.parent
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=http.server.ThreadingHTTPServer(("127.0.0.1",0),functools.partial(Q,directory=str(ROOT)))
threading.Thread(target=srv.serve_forever,daemon=True).start()
URL=f"http://127.0.0.1:{srv.server_address[1]}/{HERE.name}/project/index.html"
mode=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=os.environ.get("CHROME","/usr/bin/google-chrome"),args=["--no-sandbox","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
    page=b.new_page(viewport={"width":1080,"height":1920})
    page.on("pageerror",lambda e:print("ERR",e)); page.on("console",lambda m:print("LOG",m.text) if m.type in("error","warning") else None)
    page.goto(URL); page.evaluate("window.ready")
    def grab(t):
        page.evaluate(f"renderT({t})"); return page.screenshot(type="jpeg",quality=93)
    if mode=="frames":
        os.makedirs(sys.argv[2],exist_ok=True)
        for t in sys.argv[3:]: open(os.path.join(sys.argv[2],f"f_{float(t):06.2f}.jpg"),"wb").write(grab(float(t)))
    else:
        out,a,z=sys.argv[2],float(sys.argv[3]),float(sys.argv[4]); tmp=out[:-4]+".tmp.mp4"
        ff=subprocess.Popen(["ffmpeg","-v","error","-y","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-","-c:v","libx264","-crf","17","-preset","medium","-pix_fmt","yuv420p","-r",str(FPS),tmp],stdin=subprocess.PIPE)
        for f in range(round(a*FPS),round(z*FPS)): ff.stdin.write(grab(f/FPS))
        ff.stdin.close()
        if ff.wait()==0: os.replace(tmp,out)
    b.close()
