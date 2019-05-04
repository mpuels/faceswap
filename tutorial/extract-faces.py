#!/usr/bin/env python3

import subprocess

from config import FACE_DIR, IMG_DIR

NAMES = [
    "cage",
    "janboehmermann",
    "marcpuels",
    "trump",
]


def main():
    for name in NAMES:
        img_dir = IMG_DIR / name
        face_dir = FACE_DIR / name
        subprocess.run(["python", "../faceswap.py", "extract",
                        "-mp",
                        "-i", str(img_dir),
                        "-o", str(face_dir)])


if __name__ == "__main__":
    main()
