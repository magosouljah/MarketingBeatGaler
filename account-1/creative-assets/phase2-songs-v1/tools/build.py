"""Build, render and finish the phase2-songs-v1 videos.

From the repo root:
    python account-1/creative-assets/phase2-songs-v1/tools/build.py ID [ID ...] \
        --songs work/songs --out work/phase2-songs [--no-audio]

For each variants.json row: assembles a HyperFrames project in
work/phase2-songs/build/<id>/ (v7's lib/, assets/ and src/wheel.js, the last
one with two patches that do not change any pose), renders a 1080x1920 PNG
sequence, prepares the audio (fragment, fades, -14 LUFS, true peak <= -1 dBTP),
encodes MP4 H.264 + AAC and writes the contact sheet and QA numbers.

Needs: node/npx (hyperframes@0.9.17), Chrome, ffmpeg, numpy, soundfile,
pyloudnorm, Pillow. Linux: HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome.
"""
import argparse
import json
import re
import os
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pyloudnorm as pyln
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent.parent
V7 = HERE.parent / "choreography-lab-v2" / "hyperframes"
FPS, DUR = 30, 6.0
TARGET_LUFS, TP_LIMIT = -14.0, -1.0
FADE_IN, FADE_OUT = 0.03, 0.25

# The only edits to v7's wheel.js. Both default to v7 behaviour.
PATCHES = [
    ("renderer.setPixelRatio(1);", "renderer.setPixelRatio(rig.pixelRatio ?? 1); // phase2-songs-v1: 1.5 for 1080x1920"),
    ("  const loads = COVERS.map((name) =>",
     "  const coverList = rig.covers ?? COVERS; // phase2-songs-v1: per-video cover order\n"
     "  const loads = [...new Set(coverList)].map((name) =>"),
    ("const cover = COVERS[k % COVERS.length];", "const cover = coverList[k % coverList.length];"),
]


def run(cmd, **kw):
    print("+", " ".join(map(str, cmd)))
    subprocess.run(cmd, check=True, **kw)


def build_project(row: dict, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    shutil.copytree(V7 / "lib", dst / "lib")
    shutil.copytree(V7 / "assets", dst / "assets")
    shutil.copy(V7 / "hyperframes.json", dst / "hyperframes.json")
    src = (V7 / "src" / "wheel.js").read_text()
    for old, new in PATCHES:
        assert src.count(old) == 1, f"patch anchor not found once: {old!r}"
        src = src.replace(old, new)
    (dst / "src").mkdir()
    (dst / "src" / "wheel.js").write_text(src)
    w = {r[0]: r for r in row["words"]}
    html = (HERE / "hyperframes" / "template.html").read_text()
    end = row["endStart"]
    rep = {
        "__VARIANT_JSON__": json.dumps(row),
        "__ID__": row["id"],
        "__GROUND__": row["colors"]["ground"],
        "__INK__": row["colors"]["ink"],
        "__MUTED__": row["colors"]["muted"],
        "__WORD_LEFT__": str(row["wordLeft"]),
        "__W1__": str(w["#w1 .wt"][1]), "__W1D__": str(w["#w1 .wt"][2]),
        "__W2__": str(w["#w2 .wt"][1]), "__W2D__": str(w["#w2 .wt"][2]),
        "__W3__": str(w["#w3 .wt"][1]), "__W3D__": str(w["#w3 .wt"][2]),
        "__END__": str(end), "__ENDD__": str(round(row["duration"] - end, 4)),
        "__DUR__": str(row["duration"]),
    }
    for k, v in rep.items():
        html = html.replace(k, v)
    left = re.findall(r"__[A-Z0-9_]+__", html)
    assert not left, f"unreplaced placeholders: {left}"
    (dst / "index.html").write_text(html)
    (dst / "meta.json").write_text(json.dumps({"id": f"beatgaler-songs-{row['id']}", "name": row["id"]}))
    (dst / "package.json").write_text(json.dumps({"name": f"songs-{row['id']}", "private": True, "type": "module"}))


def render_frames(proj: Path, frames: Path) -> None:
    if frames.exists():
        shutil.rmtree(frames)
    env = {**os.environ, "HYPERFRAMES_SKIP_SKILLS": "1", "DO_NOT_TRACK": "1"}
    env.setdefault("HYPERFRAMES_BROWSER_PATH", "/usr/bin/google-chrome")
    run(["npx", "--yes", "hyperframes@0.9.17", "render", "--format", "png-sequence", "-o", str(frames), "--quiet"],
        cwd=proj, env=env)


def true_peak_db(x: np.ndarray, sr: int) -> float:
    from scipy.signal import resample_poly
    up = resample_poly(x, 4, 1, axis=0)
    return float(20 * np.log10(np.abs(up).max() + 1e-12))


def prepare_audio(wav: Path, row: dict, out: Path) -> dict:
    y, sr = sf.read(str(wav), always_2d=True)
    a, b = int(row["fragment"][0] * sr), int(round(row["fragment"][0] * sr + row["duration"] * sr))
    seg = y[a:b].astype(np.float64)
    if len(seg) < b - a:
        seg = np.vstack([seg, np.zeros((b - a - len(seg), seg.shape[1]))])
    n_in, n_out = int(FADE_IN * sr), int(FADE_OUT * sr)
    seg[:n_in] *= (0.5 - 0.5 * np.cos(np.linspace(0, np.pi, n_in)))[:, None]
    seg[-n_out:] *= (0.5 + 0.5 * np.cos(np.linspace(0, np.pi, n_out)))[:, None]
    meter = pyln.Meter(sr)
    raw = out.with_suffix(".pre.wav")
    gain_db = TARGET_LUFS - meter.integrated_loudness(seg)
    limited = False
    for _ in range(4):
        sf.write(str(raw), seg * 10 ** (gain_db / 20), sr, subtype="FLOAT")
        x, _ = sf.read(str(raw), always_2d=True)
        if true_peak_db(x, sr) > TP_LIMIT - 0.3:
            # transparent peak control: ffmpeg alimiter at -1.5 dBFS, 4x oversampled by aresample
            limited = True
            run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af",
                 f"aresample={sr * 4},alimiter=limit={10 ** (-1.6 / 20):.4f}:attack=0.5:release=40:level=disabled,aresample={sr}",
                 "-c:a", "pcm_f32le", str(out)])
        else:
            shutil.copy(raw, out)
        x, _ = sf.read(str(out), always_2d=True)
        lufs = meter.integrated_loudness(x)
        if abs(lufs - TARGET_LUFS) <= 0.1:
            break
        gain_db += TARGET_LUFS - lufs
    raw.unlink(missing_ok=True)
    return {"gain_db": round(gain_db, 2), "lufs_wav": round(lufs, 2), "true_peak_wav_dbtp": round(true_peak_db(x, sr), 2),
            "limiter": limited, "fade_in_s": FADE_IN, "fade_out_s": FADE_OUT}


def encode(frames: Path, audio: Path | None, mp4: Path, dur: float) -> None:
    # hyperframes png-sequence: frame_000001.png ... frame_000180.png
    cmd = ["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-start_number", "1",
           "-i", str(frames / "frame_%06d.png")]
    if audio:
        cmd += ["-i", str(audio)]
    cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-profile:v", "high", "-pix_fmt", "yuv420p",
            "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-movflags", "+faststart"]
    if audio:
        cmd += ["-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", str(dur)]
    run(cmd + [str(mp4)])


def measure_mp4(mp4: Path) -> dict:
    r = subprocess.run(["ffmpeg", "-nostats", "-i", str(mp4), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    txt = r.stderr.split("Summary:")[-1]
    get = lambda key: float(txt.split(key)[1].split()[0])
    return {"lufs_mp4": get("I:"), "true_peak_mp4_dbtp": get("Peak:")}


def occupancy(frames: Path, ground: str) -> list:
    g = np.array([int(ground[i:i + 2], 16) for i in (1, 3, 5)], dtype=np.int16)
    out = []
    for p in sorted(frames.glob("*.png")):
        im = np.asarray(Image.open(p).convert("RGB").resize((180, 320)), dtype=np.int16)
        out.append(round(float((np.abs(im - g).max(-1) > 40).mean()), 4))
    return out


def contact_sheet(frames: Path, row: dict, wav: Path | None, out: Path, qa: dict) -> None:
    pngs = sorted(frames.glob("*.png"))
    DURV = row["duration"]
    times = [round(0.25 * i, 2) for i in range(int(DURV / 0.25 + 1e-6) + 1) if 0.25 * i < DURV]
    tw, th, cols = 180, 320, 8
    head, wave_h = 64, 150
    W = cols * tw
    nrows = -(-len(times) // cols)
    H = head + nrows * th + wave_h
    ground = row["colors"]["ground"]
    dark = row["theme"] == "negro"
    sheet = Image.new("RGB", (W, H), "#1a1a1a")
    d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
        fb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except OSError:
        f = fb = ImageFont.load_default()
    song = row.get("song") or "v7 (sin audio)"
    d.text((10, 8), f"{row['id']}  ·  {song}  ·  fondo {ground}  ·  1080x1920 30 fps · {DURV:.2f} s", fill="white", font=fb)
    wv = row["wheel"]
    d.text((10, 36), (f"cortes {row['words'][0][1]:.3f} / {row['words'][1][1]:.3f} / {row['words'][2][1]:.3f} · titular "
                      f"{row['head']:.3f}  |  fase {wv['phaseDelta']:+.2f} rad · ritmo x{wv['omegaScale']:.2f} · "
                      f"pos {wv['dx']:+.2f},{wv['dy']:+.2f} · escala x{wv['scaleMul']:.2f}  |  "
                      f"{qa.get('lufs_mp4', '–')} LUFS · TP {qa.get('true_peak_mp4_dbtp', '–')} dBTP"),
           fill="#cfcfcf", font=f)
    for i, t in enumerate(times):
        fi = min(int(round(t * FPS)), len(pngs) - 1)
        im = Image.open(pngs[fi]).convert("RGB").resize((tw, th), Image.LANCZOS)
        x, y = (i % cols) * tw, head + (i // cols) * th
        sheet.paste(im, (x, y))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline="#444")
        d.text((x + 6, y + 4), f"{t:.2f}s  f{fi}", fill="#ffd400" if dark else "#c2410c", font=f)
    y0 = head + nrows * th
    d.rectangle([0, y0, W, H], fill="#111")
    if wav:
        y, sr = sf.read(str(wav), always_2d=True)
        m = y.mean(1)[: int(DURV * sr)]
        cols_px = np.array_split(np.abs(m), W)
        amp = np.array([c.max() if len(c) else 0 for c in cols_px])
        amp = amp / (amp.max() + 1e-9)
        mid = y0 + wave_h // 2 + 8
        for x, a in enumerate(amp):
            d.line([x, mid - a * 55, x, mid + a * 55], fill="#3a7bd5")
    for label, t, col in [("Unlimited", row["words"][0][1], "#ffd400"), ("Free*", row["words"][1][1], "#ffd400"),
                          ("Storage", row["words"][2][1], "#ffd400"), ("cierre", row["head"], "#ff5a5a"),
                          ("rueda (v7)", 1.22, "#7CFC00")]:
        x = int(t / DURV * W)
        d.line([x, y0, x, H], fill=col, width=2)
        d.text((x + 3, (H - 38) if label.startswith("rueda") else y0 + 2), f"{label} {t:.2f}", fill=col, font=f)
    for s in range(int(DURV) + 1):
        x = int(s / DURV * W)
        d.text((min(x + 2, W - 20), H - 18), f"{s}s", fill="#888", font=f)
    sheet.save(out, quality=88)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--songs", default="work/songs")
    ap.add_argument("--out", default="work/phase2-songs")
    ap.add_argument("--no-audio", action="store_true")
    ap.add_argument("--keep-frames", action="store_true")
    ap.add_argument("--reuse-frames", action="store_true")
    a = ap.parse_args()
    rows = {r["id"]: r for r in json.loads((HERE / "variants.json").read_text())}
    out = Path(a.out).resolve()
    (out / "build").mkdir(parents=True, exist_ok=True)
    sheets = HERE / "evidence" / "contact-sheets"
    qa_path = HERE / "evidence" / "qa.json"
    qa_all = json.loads(qa_path.read_text()) if qa_path.exists() else {}
    for vid in a.ids:
        row = rows[vid]
        proj = out / "build" / vid
        frames = out / "build" / f"{vid}-frames"
        if not (a.reuse_frames and len(list(frames.glob("*.png"))) == round(row["duration"] * FPS)):
            build_project(row, proj)
            render_frames(proj, frames)
        qa = {"frames": len(list(frames.glob("*.png")))}
        wav = None
        audio = None
        if row.get("song") and not a.no_audio:
            wav = Path(a.songs) / row["song"]
            audio = out / "build" / f"{vid}.wav"
            qa.update(prepare_audio(wav, row, audio))
        mp4 = out / f"beatgaler-{vid}.mp4"
        encode(frames, audio, mp4, row["duration"])
        if audio:
            qa.update(measure_mp4(mp4))
        qa["occupancy"] = occupancy(frames, row["colors"]["ground"])
        contact_sheet(frames, row, audio, sheets / f"{vid}.jpg", qa)
        qa_all[vid] = qa
        qa_path.write_text(json.dumps(qa_all, indent=1))
        if not a.keep_frames:
            shutil.rmtree(frames)
        print(vid, {k: v for k, v in qa.items() if k != "occupancy"})


if __name__ == "__main__":
    main()
