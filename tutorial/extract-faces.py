#!/usr/bin/env python3

import subprocess
from pathlib import Path
from typing import Dict, NamedTuple

import plac

from config import FACE_DIR, IMG_DIR


class ExtractFacesJob(NamedTuple):
    src: Path
    dst: Path


@plac.annotations(
    name='Name of the dataset to extract faces from. If "list", then list the'
         ' datasets.',
    dry_run=("Don't actually extract faces. Instead print the command that "
             "would have been executed.",
             "flag")
)
def main(name, dry_run):
    """Extract faces from images.

    Each folder in IMG_DIR is interpreted as a face extraction job. The
    extracted faces are written to FACE_DIR.
    """
    datasets = get_extract_faces_jobs()

    if name == 'list':
        for name_job in sorted(datasets):
            print(name_job)
            print(f'    {datasets[name_job].src}')
            print(f'    {datasets[name_job].dst}')
        return

    if name not in datasets:
        print(f'Error: Dataset "{name}" not found in "{IMG_DIR}"')
        return 1

    cmd = [
        "python", "../faceswap.py", "extract",
        "-mp",
        "-i", datasets[name].src,
        "-o", datasets[name].dst,
    ]

    if dry_run:
        print(cmd)
    else:
        datasets[name].dst.mkdir(parents=True, exist_ok=True)
        subprocess.run(cmd)


def get_extract_faces_jobs() -> Dict[str, ExtractFacesJob]:
    img_child_dirs = [child for child in Path.iterdir(IMG_DIR) if child.is_dir()]
    extract_faces_jobs = {}
    for img_child_dir in img_child_dirs:
        extract_faces_jobs[img_child_dir.stem] = ExtractFacesJob(
            img_child_dir,
            FACE_DIR / img_child_dir.stem)
    return extract_faces_jobs


if __name__ == "__main__":
    plac.call(main)
