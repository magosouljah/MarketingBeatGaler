"""Generate a deterministic synthetic test: moving square, hard cut, static hold, audio."""
import argparse
from pathlib import Path
from .pipeline import run, dump


def generate(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=False)
    # Lossless FFV1 permits repeatable content tests; not a creative reference.
    width, height, fps, count = 160, 96, 30, 60
    raw = bytearray()
    for i in range(count):
        pixels = bytearray([0 if i < 30 else 255]) * (width * height)
        if i < 30:
            x = 10 + 2 * i
            for y in range(32, 48):
                pixels[y * width + x:y * width + x + 16] = bytes([255]) * 16
        raw.extend(pixels)
    source = folder / 'pixels.gray'
    source.write_bytes(raw)
    run(['ffmpeg', '-nostdin', '-v', 'error', '-f', 'rawvideo', '-pixel_format', 'gray', '-video_size', '160x96',
         '-framerate', str(fps), '-i', source, '-f', 'lavfi', '-i', 'sine=frequency=440:sample_rate=48000:duration=2',
         '-map', '0:v', '-map', '1:a', '-c:v', 'ffv1', '-c:a', 'pcm_s16le', '-threads', '1', folder / 'source.mkv'])
    source.unlink()
    truth = {'synthetic': True, 'fps': fps, 'frame_count': count, 'cut_frame': 30,
             'square': {'frames': [0, 29], 'x_left_pixels': '10 + 2*frame', 'y_top_pixels': 32,
                        'size_pixels': 16, 'vx_pixels_per_second': 60},
             'hold_frames': [30, 59], 'audio': '440Hz continuous tone; not a beat detector test'}
    dump(folder / 'ground-truth.json', truth)
    dump(folder / 'tracks.json', [{'id': 'square-center', 'evidence': 'Synthetic generator truth; coordinates in coded 160x96 image.',
                                 'uncertainty': 'Generator truth supplied for demonstration; real reference needs manual tracking error bounds.',
                                 'samples': [{'frame': i, 'x': (18+2*i)/160, 'y': 40/96} for i in (0, 10, 20)]}])
    return folder / 'source.mkv'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder')
    generate(parser.parse_args().folder)
