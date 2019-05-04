#!/usr/bin/env python3

import subprocess

from config import IMG_DIR, VIDEO_DIR

NAMES = [
    "cage",
    "janboehmermann",
    "marcpuels",
    "trump",
]


def main():
    for name in NAMES:
        img_dir = IMG_DIR / name
        img_dir.mkdir(parents=True, exist_ok=True)
        for video in (VIDEO_DIR / name).glob("*"):
            subprocess.run(["ffmpeg",
                            "-i",
                            video,
                            img_dir / f"{video.stem}-%04d.png"])


if __name__ == "__main__":
    main()
