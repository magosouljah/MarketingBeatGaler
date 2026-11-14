from pathlib import Path
from PIL import Image

folder = Path("assets/covers")
exts = {".jpg", ".jpeg", ".png", ".webp", ".avif"}

files = sorted([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in exts])

for i, path in enumerate(files, start=1):
    with Image.open(path) as img:
        w, h = img.size
        side = min(w, h)

        left = (w - side) // 2
        top = (h - side) // 2
        right = left + side
        bottom = top + side

        cropped = img.crop((left, top, right, bottom))

        ext = path.suffix.lower()
        if ext == ".jpeg":
            ext = ".jpg"

        new_name = f"cover-{i:03d}{ext}"
        out_path = folder / new_name

        if cropped.mode not in ("RGB", "RGBA"):
            cropped = cropped.convert("RGB")

        if ext in [".jpg", ".jpeg"]:
            cropped.save(out_path, quality=95)
        else:
            cropped.save(out_path)

        if out_path.resolve() != path.resolve():
            path.unlink()

print(f"Done. Processed {len(files)} images.")