#!/usr/bin/env python3
"""Dibuja sobre un frame 1080x1920 lo que Instagram tapa o recorta en un iPhone alto.

    python shared/technical-qa/phone_guide.py frame.png [salida.jpg]

Rosa = no se ve o queda bajo la interfaz. Medido el 2026-11-14 sobre una captura real
(iPhone con isla dinamica, Reel abierto desde un mensaje): ver INSTAGRAM-SAFE-ZONES.md.
Usarlo sobre los frames clave ANTES de un render largo.
"""
import sys

from PIL import Image, ImageDraw

SIDE = 49            # px que se recortan a cada lado
TOP = 250            # isla + barra superior de Instagram
ISLAND = (390, 33, 695, 154)
BUTTONS = (915, 1208, 990, 1858)   # me gusta / comentar / compartir / guardar
CAPTION_Y = 1683                   # usuario y descripcion


def main():
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else src.rsplit(".", 1)[0] + "-phone.jpg"
    im = Image.open(src).convert("RGB")
    if im.size != (1080, 1920):
        im = im.resize((1080, 1920))
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    pink, soft = (255, 0, 90, 255), (255, 0, 90, 70)
    d.rectangle([0, 0, SIDE - 1, 1919], fill=pink)
    d.rectangle([1080 - SIDE, 0, 1079, 1919], fill=pink)
    d.rectangle([SIDE, 0, 1080 - SIDE - 1, TOP], fill=soft)
    d.rounded_rectangle(ISLAND, radius=60, fill=pink)
    d.rectangle(BUTTONS, fill=soft)
    d.rectangle([SIDE, CAPTION_Y, 1080 - SIDE - 1, 1919], fill=soft)
    d.line([SIDE, TOP, 1080 - SIDE, TOP], fill=pink, width=3)
    Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB").save(dst, quality=90)
    print("OK ", dst)


if __name__ == "__main__":
    main()
