#!/usr/bin/env python3
"""Tiempos exactos de cada palabra de una locucion cuyo texto ya se conoce.

    python shared/transcription/align_words.py voz.wav "you have hundreds of beats"
    python shared/transcription/align_words.py voz.wav "comment galer to try it for free" --say galer="G AA L ER"

Imprime una linea por palabra (inicio y fin en segundos dentro del archivo) y, debajo,
dos tiras de control de 30 ms por caracter: energia (#, +, .) y sibilantes (S).
Las sibilantes sirven para comprobar el resultado a ojo: el final de "hundredS",
"beaTS" o "whiCH" tiene que coincidir con una S.

Por que existe: en add-finder se ubicaron las palabras mirando solo el volumen y
"beats" quedo partido en dos (la "b-ea" se tomo por "of" y la "ts" por "beats").
El texto en pantalla salio 6-9 frames tarde y el propietario lo noto. Una alineacion
forzada contra el texto lo resuelve en segundos.

Requiere: pip install pocketsphinx numpy ; ffmpeg en el PATH. Solo ingles (modelo en-us).
Palabras fuera del diccionario: pasarlas con --say palabra="FONEMAS ARPABET".
"""
import argparse
import os
import subprocess
import sys

import numpy as np


def pcm16k(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ar", "16000", "-ac", "1", "-f", "s16le", "-"],
                         check=True, capture_output=True).stdout
    return out


def align(raw, text, extra):
    from pocketsphinx import Decoder, get_model_path
    mp = get_model_path()
    d = Decoder(hmm=os.path.join(mp, "en-us/en-us"), dict=os.path.join(mp, "en-us/cmudict-en-us.dict"), loglevel="FATAL")
    for word in text.split():
        if d.lookup_word(word) is None:
            if word not in extra:
                sys.exit(f'"{word}" no esta en el diccionario: agrega --say {word}="FONEMAS"')
            d.add_word(word, extra[word], True)
    d.set_align_text(text)
    d.start_utt()
    d.process_raw(raw, full_utt=True)
    d.end_utt()
    return [(s.word, s.start_frame / 100, s.end_frame / 100) for s in d.seg() if s.word not in ("<sil>", "(NULL)", "<s>", "</s>")]


def strips(raw, step=0.03, sr=16000):
    x = np.frombuffer(raw, dtype="<i2").astype(float)
    n = 512
    hop = int(step * sr)
    energy, sib = "", ""
    frames = [x[i:i + n] for i in range(0, max(1, len(x) - n), hop)]
    spec = [np.abs(np.fft.rfft(f * np.hanning(len(f)), n)) for f in frames if len(f) == n]
    if not spec:
        return "", ""
    tot = np.array([s.sum() for s in spec])
    hi = np.array([s[int(4000 / (sr / n)):].sum() for s in spec])
    m = tot.max() or 1.0
    for t, h in zip(tot, hi):
        energy += "#" if t > 0.2 * m else ("+" if t > 0.06 * m else ".")
        sib += "S" if (h > 0.45 * t and t > 0.04 * m) else " "
    return energy, sib


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio")
    ap.add_argument("text")
    ap.add_argument("--say", action="append", default=[], metavar='palabra="FONEMAS"')
    ap.add_argument("--offset", type=float, default=0.0, help="segundo del video en que empieza este audio")
    a = ap.parse_args()
    extra = dict(s.split("=", 1) for s in a.say)
    text = a.text.lower()
    raw = pcm16k(a.audio)
    for word, start, end in align(raw, text, extra):
        line = f"{word:<12} {start:6.2f} - {end:5.2f} s"
        if a.offset:
            line += f"   -> video {start + a.offset:6.2f} s (frame {round((start + a.offset) * 30)} a 30 fps)"
        print(line)
    energy, sib = strips(raw)
    print("\nenergia   ", energy)
    print("sibilantes", sib)
    print("          ", "".join(str((i // 10) % 10) if i % 10 == 0 else "-" for i in range(len(energy))), " (cada 10 caracteres = 0.3 s)")


if __name__ == "__main__":
    main()
