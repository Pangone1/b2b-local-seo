import os
import sys
from PIL import Image

priority_dirs = [
    "/storage/emulated/0/Pictures/.thumbnails",
    "/storage/emulated/0/Pictures/.thumbnail",
    "/storage/emulated/0/pictures/.thumbnails",
    "/storage/emulated/0/pictures/.thumbnail",
]

src_path = None
for d in priority_dirs:
    candidate = os.path.join(d, "5416.jpg")
    if os.path.isfile(candidate):
        src_path = candidate
        break

if not src_path:
    for d in priority_dirs:
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.lower().startswith("5416."):
                    src_path = os.path.join(d, fn)
                    break
        if src_path:
            break

if not src_path:
    print("ERROR: 5416.jpg not found in /storage/emulated/0/Pictures/.thumbnails or .thumbnail")
    for d in priority_dirs:
        if os.path.isdir(d):
            print("Files in", d, ":", sorted(os.listdir(d))[-10:])
    sys.exit(1)

print(f"SOURCE_IMAGE: {src_path}")

img = Image.open(src_path).convert("RGB")
w, h = img.size

top = int(h * 0.04)
bottom = int(h * 0.52)
cropped = img.crop((0, top, w, bottom))

target_w = 1920
target_h = int(cropped.height * (target_w / cropped.width))
final_banner = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
final_banner.save("banner.jpg", "JPEG", quality=92, optimize=True)
print(f"SAVED_BANNER: banner.jpg ({target_w}x{target_h})")
