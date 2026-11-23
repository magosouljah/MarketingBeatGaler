#!/usr/bin/env python3
"""Deja project/assets listo para renderizar add-finder.

Uso (desde cualquier carpeta):  python content/videos/add-finder/tools/prepare.py

Hace cuatro cosas, todas repetibles:
  1. Copia las 60 portadas compartidas a project/assets/covers.
  2. Instala gsap (npm) y copia gsap.min.js a project/assets.
  3. Recorta los iconos de archivo .als y .flp desde las capturas de inputs/.
  4. Recorta las cuatro frases de voz y copia el beat desde inputs/.

Los archivos de inputs/ NO estan en el repositorio (ver inputs/README.md).
Requiere: Python 3.10+, Pillow, numpy, ffmpeg, Node 22+.
"""
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # content/videos/add-finder
PROJECT = HERE / "project"
ASSETS = PROJECT / "assets"
INPUTS = HERE / "inputs"
COVERS = HERE.parent.parent / "assets" / "covers"

# archivo en inputs/ -> (salida, inicio s, duracion s, filtro extra)
VOICE = {
    "you_have_hundreds_of_beats.mp3": ("l1a.wav", 0.13, 1.98, "afade=t=out:st=1.9:d=0.08"),
    "but_no_idea_wich_ones_wich..mp3": ("l1b.wav", 0.11, 2.08, "afade=t=out:st=2.0:d=0.08"),
    "theres_a_better_way.mp3": ("l2.wav", 0.08, 0.98, "volume=5dB,afade=t=out:st=0.9:d=0.08"),
    "comment_galer_to_try_it_for_free.mp3": ("l3.wav", 0.12, 2.72, None),
}
BEAT = "beat_galer_COCObongo.mp3"                      # segunda version: 33.7 s, 147 BPM
ICONS = {"als.png": 39, "flp.png": 18}                 # captura -> px a quitar abajo (el nombre del archivo)


def run(cmd, **kw):
    print("  $", " ".join(str(c) for c in cmd))
    subprocess.run(cmd, check=True, **kw)


def covers():
    out = ASSETS / "covers"
    out.mkdir(parents=True, exist_ok=True)
    files = sorted(COVERS.glob("cover-*.jpg"))
    if len(files) != 60:
        sys.exit(f"Se esperaban 60 portadas en {COVERS}, hay {len(files)}")
    for f in files:
        shutil.copy2(f, out / f.name)
    print(f"portadas: {len(files)} copiadas")


def gsap():
    if not (PROJECT / "node_modules" / "gsap").exists():
        run(["npm", "install", "--silent"], cwd=PROJECT)
    shutil.copy2(PROJECT / "node_modules" / "gsap" / "dist" / "gsap.min.js", ASSETS / "gsap.min.js")
    print("gsap: copiado")


def icon(src, dst, bottom_cut):
    """Quita el fondo blanco por relleno desde los bordes y deja un PNG cuadrado de 256 px."""
    import numpy as np
    from PIL import Image
    im = Image.open(src).convert("RGB")
    w, h = im.size
    im = im.crop((0, 0, w, h - bottom_cut))
    a = np.asarray(im).astype(int)
    white = a.min(axis=2) > 236
    H, W = white.shape
    seen = np.zeros_like(white)
    stack = [(y, x) for y in range(H) for x in (0, W - 1)] + [(y, x) for x in range(W) for y in (0, H - 1)]
    while stack:
        y, x = stack.pop()
        if y < 0 or x < 0 or y >= H or x >= W or seen[y, x] or not white[y, x]:
            continue
        seen[y, x] = True
        stack += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    rgba = np.dstack([a.astype(np.uint8), np.where(seen, 0, 255).astype(np.uint8)])
    out = Image.fromarray(rgba, "RGBA")
    out = out.crop(out.getbbox())
    s = max(out.size)
    sq = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    sq.paste(out, ((s - out.size[0]) // 2, (s - out.size[1]) // 2))
    sq.resize((256, 256), Image.LANCZOS).save(dst)


def icons():
    out = ASSETS / "icons"
    out.mkdir(parents=True, exist_ok=True)
    for name, cut in ICONS.items():
        src = INPUTS / name
        if not src.exists():
            sys.exit(f"Falta {src} (ver inputs/README.md)")
        icon(src, out / name, cut)
    print("iconos: als.png, flp.png")


def audio():
    vo = ASSETS / "vo"
    vo.mkdir(parents=True, exist_ok=True)
    for name, (dst, ss, dur, extra) in VOICE.items():
        src = INPUTS / name
        if not src.exists():
            sys.exit(f"Falta {src} (ver inputs/README.md)")
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-t", str(dur), "-i", str(src)]
        if extra:
            cmd += ["-af", extra]
        run(cmd + [str(vo / dst)])
    beat = INPUTS / BEAT
    if not beat.exists():
        sys.exit(f"Falta {beat} (ver inputs/README.md)")
    shutil.copy2(beat, ASSETS / "beat.mp3")
    print("audio: 4 voces recortadas + beat")


if __name__ == "__main__":
    covers()
    gsap()
    icons()
    audio()
    print("Listo. Siguiente: tools/render.sh")
