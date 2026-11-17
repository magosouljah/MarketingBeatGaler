#!/usr/bin/env python3
"""Filma project/index.html con Chrome (Playwright).

    render.py frames <dir_salida> t1 t2 ...      frames sueltos (JPEG) en tiempo de video
    render.py seg <salida.mp4> t_ini t_fin       un tramo codificado a 30 fps

URL de la pagina en BASE_URL (por defecto http://127.0.0.1:8765/index.html). Chrome en CHROME.
"""
import base64
import os
import subprocess
import sys
from playwright.sync_api import sync_playwright

FPS = 30
URL = os.environ.get('BASE_URL', 'http://127.0.0.1:8765/index.html')
mode = sys.argv[1]
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=os.environ.get('CHROME') or None, args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1080, 'height': 1920})
    page.on('pageerror', lambda e: print('ERR', e))
    page.goto(URL)
    page.evaluate('window.ready')
    grab = lambda t: base64.b64decode(page.evaluate(f"(renderT({t}), document.getElementById('c').toDataURL('image/jpeg',0.92).split(',')[1])"))
    if mode == 'frames':
        for t in sys.argv[3:]:
            open(os.path.join(sys.argv[2], f'f_{float(t):05.2f}.jpg'), 'wb').write(grab(float(t)))
    else:
        out, a, z = sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
        tmp = out[:-4] + '.tmp.mp4'
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                               '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', str(FPS), tmp], stdin=subprocess.PIPE)
        for f in range(round(a * FPS), round(z * FPS)):
            ff.stdin.write(grab(f / FPS))
        ff.stdin.close()
        if ff.wait() == 0:
            os.replace(tmp, out)
    browser.close()
