"""Write variants.json: the 8 videos (4 songs x black/white) of phase2-songs-v1.

    python account-1/creative-assets/phase2-songs-v1/tools/plan_variants.py

Inputs: evidence/audio-analysis.json (audio_cuts.py). Every value that makes a
video unique is in VARIATION below, chosen by hand inside the owner's limits
(small changes that keep the approved v7: cover order/selection, initial wheel
angle, rhythm and position within +-5 %, slightly different word entrances).
The stack (3.75-4.8 s) is never touched. Row "v7" reproduces the approved film.
"""
import json
import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
COVERS = [f"cover-{i:02d}.jpg" for i in range(1, 21)] + [f"cover-{i:02d}.avif" for i in range(21, 25)]
V7_COVERS = [COVERS[k % 24] for k in range(28)]

THEMES = {
    "negro": {"ground": "#0C0C0C", "ink": "#FFFFFF", "muted": "rgba(255, 255, 255, 0.62)"},
    # proposal: warm paper white (pure white glares in dark-mode feeds); ink is
    # the black version's ground, so the two versions mirror each other
    "blanco": {"ground": "#F3F1EC", "ink": "#0C0C0C", "muted": "rgba(12, 12, 12, 0.60)"},
}

# v7 values: phaseDelta 0, omegaScale 1, dx/dy 0, scaleMul 1, word entrance
# y 26 / rot -3.5 / from 0.85 / 0.16 s, word left 14 px, brand x -40.
VARIATION = [
    # id, song index, theme, phaseDelta rad, omegaScale, dx, dy (world), scaleMul, cover seed, word (y, rot, from, dur), word left px, brand x
    ("01-c1-negro", 0, "negro", 0.12, 1.00, 0.03, 0.00, 1.00, 11, (26, -3.5, 0.85, 0.16), 14, -40),
    ("02-c1-blanco", 0, "blanco", -0.20, 1.02, -0.04, 0.02, 0.98, 12, (22, 3.0, 0.86, 0.15), 8, -34),
    ("03-c2-negro", 1, "negro", 0.30, 0.98, 0.05, -0.02, 1.02, 21, (30, -4.5, 0.84, 0.17), 18, -46),
    ("04-c2-blanco", 1, "blanco", -0.35, 1.03, -0.02, -0.03, 0.99, 22, (20, -2.5, 0.87, 0.14), 12, -36),
    ("05-c3-negro", 2, "negro", 0.45, 0.97, -0.05, 0.02, 1.01, 31, (28, 3.5, 0.85, 0.18), 10, -42),
    ("06-c3-blanco", 2, "blanco", -0.10, 1.01, 0.02, 0.03, 1.03, 32, (24, -3.0, 0.83, 0.16), 16, -38),
    ("07-c4-negro", 3, "negro", 0.22, 1.04, 0.00, -0.04, 0.97, 41, (32, -4.0, 0.86, 0.15), 20, -44),
    ("08-c4-blanco", 3, "blanco", -0.50, 0.99, 0.04, 0.01, 1.00, 42, (26, 2.5, 0.84, 0.17), 6, -32),
]


# v7 keeps "Free*" on screen 0.04 s after "Storage" cuts in (w2 lasts 0.87 s,
# the next cut is 0.83 s later: 1-2 frames with both words). Preserved because
# v7 is approved; reported to the owner as an open point.
W2_OVERLAP = 0.04


def cover_order(seed: int) -> list:
    """All 24 covers shuffled, then 4 repeats; no cover next to itself on the ring."""
    rng = random.Random(seed)
    base = COVERS[:]
    rng.shuffle(base)
    while True:
        extra = rng.sample(base, 4)
        ring = base + extra
        if all(ring[i] != ring[(i + 1) % 28] and ring[i] != ring[(i + 2) % 28] for i in range(28)):
            return ring


def row(vid, song, theme, cuts, wheel, covers, word, wleft, bx, song_name=None):
    w1, w2, w3, head = cuts["w1"]["t"], cuts["w2"]["t"], cuts["w3"]["t"], cuts["head"]["t"]
    return {
        "id": vid,
        "song": song_name,
        "theme": theme,
        "colors": THEMES[theme],
        "words": [["#w1 .wt", w1, round(w2 - w1, 4)], ["#w2 .wt", w2, round(w3 - w2 + W2_OVERLAP, 4)], ["#w3 .wt", w3, 0.62]],
        "head": head,
        "endStart": round(head - 0.07, 4),
        "wordIn": {"y": word[0], "rot": word[1], "from": word[2], "dur": word[3]},
        "wordLeft": wleft,
        "brandX": bx,
        "wheel": {"until": 3.46, **wheel},
        "covers": covers,
        "duration": 6.0,
    }


def main() -> None:
    analysis = json.loads((HERE / "evidence/audio-analysis.json").read_text())
    songs = analysis["songs"]
    rows = []
    nominal = {k: {"t": t} for k, t in {"w1": 1.53, "w2": 2.20, "w3": 3.03, "head": 4.37}.items()}
    rows.append(row("v7", None, "negro", nominal,
                    {"phaseDelta": 0.0, "omegaScale": 1.0, "dx": 0.0, "dy": 0.0, "scaleMul": 1.0},
                    V7_COVERS, (26, -3.5, 0.85, 0.16), 14, -40))
    for vid, si, theme, ph, om, dx, dy, sc, seed, word, wl, bx in VARIATION:
        s = songs[si]
        r = row(vid, si, theme, s["cuts"], {"phaseDelta": ph, "omegaScale": om, "dx": dx, "dy": dy, "scaleMul": sc},
                cover_order(seed), word, wl, bx, song_name=s["file"])
        # owner 2026-11-07: "alargar todo el video hasta que finalice la canción":
        # the film lasts until the WAV ends (rounded up to a whole frame); the
        # extra time is end card, the wheel choreography is unchanged
        frames = math.ceil(s["duration_s"] * 30 - 1e-6)
        r["duration"] = round(frames / 30, 4)
        r["fragment"] = [0.0, s["duration_s"]]
        r["lufs_fragment"] = s["lufs_fragment"]
        rows.append(r)
    (HERE / "variants.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f"{len(rows)} rows -> variants.json")


if __name__ == "__main__":
    main()
