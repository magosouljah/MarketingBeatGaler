#!/usr/bin/env python3
"""Golpes reales de un beat: donde caen de verdad los kicks y las cajas.

    python shared/editing/find_hits.py beat.mp3
    python shared/editing/find_hits.py beat.mp3 --desde 3 --hasta 16 --offset -0.546

Imprime los transientes graves (kick/808, <150 Hz) y medios (caja/clap, 150-2500 Hz)
con su fuerza relativa, y un perfil de energia cada 0.5 s para ver intro, subida,
silencios y drop. Con --offset convierte tiempo de archivo a tiempo de video.

Por que existe: en add-finder los impactos se anclaron primero a una rejilla teorica
de compases (BPM x 4). El MP3 traia ~35 ms de retraso y el patron real de kicks no
caia en los tiempos fuertes, asi que el golpe visual quedo en mitad de un redoble.
Regla validada: animar contra transientes medidos, nunca contra segundos redondos.

Requiere: pip install librosa numpy.
"""
import argparse

import librosa
import numpy as np


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio")
    ap.add_argument("--desde", type=float, default=0.0)
    ap.add_argument("--hasta", type=float, default=None)
    ap.add_argument("--offset", type=float, default=0.0, help="se suma a cada tiempo (archivo -> video)")
    ap.add_argument("--umbral", type=float, default=0.25, help="fuerza minima relativa al golpe mas fuerte")
    a = ap.parse_args()

    y, sr = librosa.load(a.audio, sr=44100, mono=True)
    hop = 128
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=hop))
    f = librosa.fft_frequencies(sr=sr, n_fft=2048)
    t = librosa.frames_to_time(np.arange(S.shape[1]), sr=sr, hop_length=hop)
    end = a.hasta if a.hasta is not None else len(y) / sr

    def hits(lo, hi, thr):
        e = S[(f >= lo) & (f < hi)].sum(0)
        d = np.maximum(0, np.diff(e, prepend=e[0]))
        m = d.max() or 1.0
        out, last = [], -1.0
        for i in range(2, len(d) - 2):
            if a.desde <= t[i] <= end and d[i] > thr * m and d[i] == d[i - 2:i + 3].max() and t[i] - last > 0.09:
                out.append((t[i], d[i] / m))
                last = t[i]
        return out

    for name, lo, hi, thr in (("KICK / 808 (<150 Hz)", 20, 150, a.umbral), ("CAJA / CLAP (150-2500 Hz)", 150, 2500, a.umbral + 0.05)):
        print(name)
        for when, strength in hits(lo, hi, thr):
            v = when + a.offset
            print(f"  {when:7.3f} s  fuerza {strength:.2f}" + (f"   -> video {v:7.3f} s (frame {round(v * 30)})" if a.offset else ""))
    rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=512)[0]
    tr = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=512)
    print("\nENERGIA cada 0.5 s")
    for s in np.arange(a.desde, end, 0.5):
        k = (tr >= s) & (tr < s + 0.5)
        if k.any():
            v = float(rms[k].mean())
            print(f"  {s:6.1f} s  {v:.3f}  " + "#" * int(v * 50))


if __name__ == "__main__":
    main()
