#!/usr/bin/env python3
"""Prepara project/assets/ y out/mix.wav a partir de inputs/ y de un checkout de BeatGaler.

    BEATGALER_REPO=/ruta/a/beatgaler python content/videos/fuck/tools/prepare.py

Requiere Pillow, numpy, scipy y FFmpeg. Nada de lo que genera se versiona (ver .gitignore).
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter
from scipy import ndimage as ndi

HERE = Path(__file__).resolve().parent.parent
INP, A, OUT = HERE / 'inputs', HERE / 'project' / 'assets', HERE / 'out'
BG = Path(os.environ.get('BEATGALER_REPO', ''))

# Portadas de DESIGN/shared/assets/real-covers. Se omiten las que muestran personajes o marcas de terceros.
COVERS = ['01', '03', '04', '05', '07', '08', '09', '11', '12', '13', '14', '15', '16', '19']
# Voz: (inicio, fin) en el archivo y entrada en el video, en segundos. Cortes en los silencios del archivo.
VOICE = [(0.00, 3.05, 0.10), (3.48, 4.12, 4.45), (4.14, 4.96, 6.15), (4.98, 5.67, 7.60), (5.66, 7.10, 8.65), (7.48, 9.80, 10.40)]
BEAT_START, DUR = 7.94, 12.9  # el golpe del drop esta en 13.94 s del beat -> cae en 6.00 s del video


def need(name):
    path = INP / name
    if not path.exists():
        sys.exit(f'Falta inputs/{name} (ver inputs/README.md)')
    return path


def tile(src, out, frac):
    """Logo centrado sobre una ficha blanca cuadrada; index.html le pone las esquinas de icono de app."""
    im = Image.open(src).convert('RGBA')
    flat = Image.new('RGBA', im.size, (255, 255, 255, 255)); flat.alpha_composite(im); rgb = flat.convert('RGB')
    box = ImageChops.difference(rgb, Image.new('RGB', rgb.size, (255, 255, 255))).point(lambda v: 255 if v > 12 else 0).getbbox()
    logo = rgb.crop(box); size = 768; w = int(size * frac); h = int(logo.height * w / logo.width)
    sheet = Image.new('RGB', (size, size), (255, 255, 255)); sheet.paste(logo.resize((w, h), Image.LANCZOS), ((size - w) // 2, (size - h) // 2))
    sheet.save(out)


def cut_white(src, thr):
    """Quita el fondo blanco conectado al borde (no los blancos interiores del objeto)."""
    im = Image.open(src).convert('RGB'); a = np.asarray(im)
    lab, _ = ndi.label(a.min(2) >= thr)
    border = (set(lab[0]) | set(lab[-1]) | set(lab[:, 0]) | set(lab[:, -1])) - {0}
    bg = ndi.binary_dilation(np.isin(lab, list(border)), iterations=1)
    out = im.convert('RGBA'); out.putalpha(Image.fromarray((~bg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)))
    return out


def images():
    A.mkdir(parents=True, exist_ok=True)
    tile(need('dropbox.png'), A / 't_dropbox.png', 0.62)
    tile(need('drive.jpg'), A / 't_drive.png', 0.64)
    Image.open(need('untitled.webp')).convert('RGB').resize((768, 768), Image.LANCZOS).save(A / 't_untitled.png')  # conserva su fondo
    if not (BG / 'DESIGN').is_dir():
        sys.exit('Define BEATGALER_REPO con la ruta a un checkout de BeatGaler (solo lectura)')
    for i, k in enumerate(COVERS):
        shutil.copy(BG / f'DESIGN/shared/assets/real-covers/cover-{k}.jpg', A / f'c{i}.jpg')
    shutil.copy(BG / 'src-tauri/icons/icon.png', A / 'logo.png')
    shutil.copy(BG / 'public/beatgaler-custom-cursor.png', A / 'cursor.png')
    # Bote: foto 1080x1920 con tapa (cuerpo y tapa por separado) y papel de la segunda foto, a la misma escala.
    can = cut_white(need('bin.jpg'), 244)
    for name, box in (('bin_lid', (100, 30, 1040, 440)), ('bin_body', (80, 890, 970, can.height))):
        part = can.crop(box); part.crop(part.getbbox()).save(A / f'{name}.png')
    paper = cut_white(need('bin-paper.jpg'), 250).crop((90, 520, 680, 716)); paper = paper.crop(paper.getbbox())
    paper.resize((int(paper.width * 1.348), int(paper.height * 1.348)), Image.LANCZOS).save(A / 'bin_paper.png')
    # Nube: silueta plana blanca, vectorial (circulos), sobre la referencia del propietario.
    k = 4; mask = Image.new('L', (600 * k, 425 * k), 0); d = ImageDraw.Draw(mask)
    for x, y, r in [(225, 152, 122), (392, 192, 92), (118, 238, 82), (495, 256, 78), (215, 285, 88), (365, 285, 84), (300, 230, 110)]:
        d.ellipse([(x - r) * k, (y - r) * k, (x + r) * k, (y + r) * k], fill=255)
    cloud = Image.new('RGBA', mask.size, (255, 255, 255, 0)); cloud.putalpha(mask); cloud.crop(cloud.getbbox()).save(A / 'cloud.png')


def audio():
    OUT.mkdir(exist_ok=True)
    voice, beat = need('voice.mp3'), need('beat.mp3')
    run = lambda *cmd: subprocess.run(['ffmpeg', '-v', 'error', '-y', *map(str, cmd)], check=True)
    parts, graph = [], [f'[0:a]volume=0.66,afade=t=in:d=0.05,afade=t=out:st={DUR - 0.45}:d=0.45[m]']
    for i, (a, b, at) in enumerate(VOICE, 1):
        part = OUT / f'v{i}.wav'
        run('-ss', a, '-to', b, '-i', voice, '-af', f'afade=t=in:d=0.015,afade=t=out:st={round(b - a - 0.03, 3)}:d=0.03', '-ar', 48000, part)
        parts += ['-i', part]; ms = int(at * 1000); graph.append(f'[{i}:a]adelay={ms}|{ms}[a{i}]')
    n = len(VOICE)
    graph.append(''.join(f'[a{i}]' for i in range(1, n + 1)) + f'amix=inputs={n}:normalize=0,volume=1.45,asplit[vx][sc]')
    # Ducking suave: el propietario rechazo el de ratio 5 por brusco.
    graph.append('[m][sc]sidechaincompress=threshold=0.1:ratio=1.6:attack=60:release=500[md]')
    graph.append(f'[md][vx]amix=inputs=2:normalize=0,alimiter=limit=0.95,apad,atrim=0:{DUR}[o]')
    run('-ss', BEAT_START, '-t', DUR, '-i', beat, *parts, '-filter_complex', ';'.join(graph), '-map', '[o]', '-ar', 48000, OUT / 'mix.wav')


if __name__ == '__main__':
    images(); audio(); print('OK  assets y out/mix.wav')
