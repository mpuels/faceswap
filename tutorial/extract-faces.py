#!/usr/bin/env python3

from pathlib import Path
import subprocess


DATA_DIR = Path("~/data").expanduser()
NAMES = [
    "cage",
    "marcpuels",
    "trump",
]


def main():
    for name in NAMES:
        img_dir = DATA_DIR / "img" / name
        face_dir = DATA_DIR / "face" / name
        subprocess.run(["python", "../faceswap.py", "extract",
                        "-mp",
                        "-i", str(img_dir),
                        "-o", str(face_dir)])

if __name__ == "__main__":
    main()
