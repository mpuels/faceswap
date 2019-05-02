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
        img_dir.mkdir(parents=True, exist_ok=True)
        for video in (DATA_DIR / "video" / name).glob("*"):
            subprocess.run(["ffmpeg",
                            "-i",
                            video,
                            img_dir / f"{video.stem}-%04d.png"])


if __name__ == "__main__":
    main()
