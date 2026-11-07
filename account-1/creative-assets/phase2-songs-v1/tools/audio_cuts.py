"""Audio analysis for phase2-songs-v1: onsets, kick hits, loudness and the
proposed cut times for the centre words and the end card of wheel-v7.

Usage (from the repo root; WAVs stay in work/songs, never in Git):
    python account-1/creative-assets/phase2-songs-v1/tools/audio_cuts.py work/songs \
        account-1/creative-assets/phase2-songs-v1/evidence/audio-analysis.json

Needs: numpy, soundfile, librosa, pyloudnorm.

Rule used for every cut (nominal times are the approved v7 cuts):
  candidate = onset (spectral flux, librosa) within +-WINDOW s of the nominal cut;
  score     = onset strength * exp(-(delta / SIGMA)^2);
  pick the best candidate whose score >= MIN_SCORE, else keep the nominal time.
  Words keep at least MIN_GAP s between cuts. The end card block keeps v7's
  0.07 s lead over the headline cut.
"""
import json
import sys
from pathlib import Path

import librosa
import numpy as np
import pyloudnorm as pyln
import soundfile as sf

NOMINAL = {"w1": 1.53, "w2": 2.20, "w3": 3.03, "head": 4.37}
WINDOW = {"w1": 0.18, "w2": 0.18, "w3": 0.18, "head": 0.15}
SIGMA = 0.10
MIN_SCORE = 2.0
MIN_GAP = 0.50
FRAGMENT = (0.0, 6.0)  # seconds of the WAV used for the 6 s film
SR = 22050


def analyse(path: Path) -> dict:
    y, sr = sf.read(str(path), always_2d=True)
    mono = y.mean(1)
    full_lufs = pyln.Meter(sr).integrated_loudness(y)
    a, b = int(FRAGMENT[0] * sr), int(FRAGMENT[1] * sr)
    frag_lufs = pyln.Meter(sr).integrated_loudness(y[a:b])
    yl = librosa.resample(mono, orig_sr=sr, target_sr=SR)
    oenv = librosa.onset.onset_strength(y=yl, sr=SR)
    times = librosa.times_like(oenv, sr=SR)
    onsets = librosa.onset.onset_detect(onset_envelope=oenv, sr=SR, units="time")
    ons = [(float(t), float(oenv[np.argmin(abs(times - t))])) for t in onsets]
    tempo, beats = librosa.beat.beat_track(onset_envelope=oenv, sr=SR, units="time")
    # the loudest onset in 1.0-1.6 s: the drop each song places on the page burst
    drop = max((o for o in ons if 1.0 <= o[0] <= 1.6), key=lambda o: o[1], default=None)
    cuts, prev = {}, None
    for key, nom in NOMINAL.items():
        best = None
        for t, s in ons:
            d = t - nom
            if abs(d) > WINDOW[key]:
                continue
            if prev is not None and t - prev < MIN_GAP:
                continue
            sc = s * np.exp(-((d / SIGMA) ** 2))
            if sc >= MIN_SCORE and (best is None or sc > best[2]):
                best = (t, s, sc)
        if best:
            t = round(best[0] * 30) / 30  # land on a video frame
            cuts[key] = {"t": round(t, 4), "onset": round(best[0], 3), "strength": round(best[1], 2),
                         "delta_frames": round((t - nom) * 30), "snapped": True}
        else:
            cuts[key] = {"t": nom, "onset": None, "strength": None, "delta_frames": 0, "snapped": False}
        prev = cuts[key]["t"]
    return {
        "file": path.name,
        "duration_s": round(len(mono) / sr, 4),
        "sample_rate": sr,
        "lufs_full": round(full_lufs, 2),
        "lufs_fragment": round(frag_lufs, 2),
        "peak_dbfs": round(20 * np.log10(np.abs(y).max() + 1e-12), 2),
        "tempo_bpm_estimate": round(float(np.atleast_1d(tempo)[0]), 1),
        "beats": [round(float(x), 3) for x in beats],
        "onsets": [[round(t, 3), round(s, 2)] for t, s in ons],
        "drop": {"t": round(drop[0], 3), "strength": round(drop[1], 2)} if drop else None,
        "fragment": list(FRAGMENT),
        "cuts": cuts,
    }


def main() -> None:
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    res = {"rule": __doc__.split("Rule used")[1].strip(), "songs": [analyse(p) for p in sorted(src.glob("*.wav"))]}
    out.write_text(json.dumps(res, indent=1, ensure_ascii=False))
    for s in res["songs"]:
        c = s["cuts"]
        print(f"{s['file']:42s} dur {s['duration_s']:.3f}  drop {s['drop']}  "
              + "  ".join(f"{k} {v['t']:.3f}({v['delta_frames']:+d}f,{v['strength']})" for k, v in c.items())
              + f"  LUFS frag {s['lufs_fragment']}")


if __name__ == "__main__":
    main()
