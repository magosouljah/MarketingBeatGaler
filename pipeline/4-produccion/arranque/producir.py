#!/usr/bin/env python3
"""Produce el arranque de una pieza y, si se le da el cuerpo, la pieza completa.

    python pipeline/4-produccion/arranque/producir.py P-0001
    python pipeline/4-produccion/arranque/producir.py P-0001 --cuerpo /ruta/add-finder.mp4 --desde 4.8

Lee ordenes/<pieza>.json, filma index.html con Chrome (Playwright) y deja en out/:
    <pieza>-arranque.mp4          solo el arranque, con pista de silencio
    <pieza>.mp4                   arranque + cuerpo desde el segundo indicado (si hay --cuerpo)
    <pieza>-frames.mp4            copia de revision con contador de frames
out/ no se versiona. Requiere: playwright, Chrome (variable CHROME) y FFmpeg.
"""
import argparse
import base64
import functools
import http.server
import json
import os
import subprocess
import sys
import threading
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
FPS = 30
SAFE = (120, 1590)  # margenes de atencion verticales del propietario


def validar(orden):
    a = orden['arranque']
    if not 0 < a['duracion'] <= 6:
        raise ValueError('duracion fuera de rango')
    for e in a['elementos']:
        if e['tipo'] not in ('texto', 'contador', 'campo'):
            raise ValueError(f"tipo desconocido: {e['tipo']}")
        alto = e.get('size', 132) / 2
        if e['y'] - alto < SAFE[0] or e['y'] + alto > SAFE[1]:
            raise ValueError(f"elemento fuera de la zona util: {e}")
    return a


def filmar(pieza, orden, salida):
    from playwright.sync_api import sync_playwright
    manejador = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(AQUI))
    manejador.log_message = lambda *a, **k: None
    servidor = http.server.ThreadingHTTPServer(('127.0.0.1', 0), manejador)
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{servidor.server_address[1]}/index.html?orden=ordenes/{pieza}.json'
    tmp = salida.with_suffix('.tmp.mp4')
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(executable_path=os.environ.get('CHROME', '/usr/bin/google-chrome'), args=['--no-sandbox'])
            pag = nav.new_page(viewport={'width': 1080, 'height': 1920})
            errores = []
            pag.on('pageerror', lambda e: errores.append(str(e)))
            pag.goto(url)
            pag.evaluate('window.ready')
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                                   '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-shortest',
                                   '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', str(FPS),
                                   '-c:a', 'aac', '-b:a', '192k', str(tmp)], stdin=subprocess.PIPE)
            for f in range(round(orden['duracion'] * FPS)):
                ff.stdin.write(base64.b64decode(pag.evaluate(
                    f"(renderT({f / FPS}), document.getElementById('c').toDataURL('image/jpeg',0.93).split(',')[1])")))
            ff.stdin.close()
            nav.close()
            if errores:
                raise RuntimeError('La pagina fallo: ' + '; '.join(errores))
            if ff.wait() != 0:
                raise RuntimeError('FFmpeg no pudo codificar el arranque')
        os.replace(tmp, salida)
    finally:
        servidor.shutdown()


def unir(arranque, cuerpo, desde, salida):
    """Arranque + cuerpo desde `desde` segundos, recodificado a 1080x1920 30 fps con un tope de 8 Mbps."""
    filtro = (f"[1:v]trim=start={desde},setpts=PTS-STARTPTS,scale=1080:1920,fps={FPS},format=yuv420p[bv];"
              f"[1:a]atrim=start={desde},asetpts=PTS-STARTPTS,aresample=48000[ba];"
              f"[0:v]format=yuv420p[av];[av][0:a][bv][ba]concat=n=2:v=1:a=1[v][a]")
    tmp = salida.with_suffix('.tmp.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(arranque), '-i', str(cuerpo), '-filter_complex', filtro,
                    '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '17', '-maxrate', '8M', '-bufsize', '16M',
                    '-preset', 'medium', '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', str(tmp)], check=True)
    os.replace(tmp, salida)


def main():
    ap = argparse.ArgumentParser(description='Produce el arranque de una pieza')
    ap.add_argument('pieza')
    ap.add_argument('--cuerpo', type=Path, help='MP4 del cuerpo ya terminado (con audio)')
    ap.add_argument('--desde', type=float, default=0.0, help='segundo del cuerpo donde empieza el producto')
    args = ap.parse_args()
    ruta = AQUI / 'ordenes' / f'{args.pieza}.json'
    orden = json.loads(ruta.read_text(encoding='utf-8'))
    if orden['pieza'] != args.pieza:
        raise SystemExit(f'{ruta} dice ser la pieza {orden["pieza"]}')
    arranque = validar(orden)
    out = AQUI / 'out'
    out.mkdir(exist_ok=True)
    clip = out / f'{args.pieza}-arranque.mp4'
    filmar(args.pieza, arranque, clip)
    final = clip
    if args.cuerpo:
        final = out / f'{args.pieza}.mp4'
        unir(clip, args.cuerpo, args.desde, final)
    subprocess.run(['bash', str(REPO / 'shared/ffmpeg/review_copy.sh'), str(final), str(out / f'{args.pieza}-frames.mp4')], check=True)
    print(f'OK  {final}')


if __name__ == '__main__':
    sys.exit(main())
