#!/usr/bin/env python3

import subprocess
from pathlib import Path
from typing import Dict, NamedTuple

import plac

from config import IMG_DIR, VIDEO_DIR


class ExtractFramesJob(NamedTuple):
    src: Path
    dst: Path


@plac.annotations(
    name="Name of the dataset to extract frames from. If 'list', then list possible values."
         "If 'all', then extract frames for all datasets.",
    dry_run=("Don't actually extract frames but print the command that would have "
             "been executed.",
             "flag")
)
def main(name, dry_run):
    datasets = get_extract_frames_jobs()

    if name == 'list':
        for name, extract_frames_job in datasets.items():
            print(name, extract_frames_job)
        return

    if name not in datasets:
        print("Error: Dataset '{}' not found in '{}'".format(name, VIDEO_DIR))
        return 1

    if name == 'all':
        extract_frames_jobs_to_execute = datasets.values()
    else:
        extract_frames_jobs_to_execute = [datasets[name]]

    for extract_frames_job in extract_frames_jobs_to_execute:
        extract_frames_job.dst.mkdir(parents=True, exist_ok=True)
        for video in extract_frames_job.src.glob("*"):
            cmd = ["ffmpeg",
                   "-i",
                   video,
                   extract_frames_job.dst / f"{video.stem}-%04d.png"]
            if dry_run:
                print(cmd)
            else:
                subprocess.run(cmd)


def get_extract_frames_jobs() -> Dict[str, ExtractFramesJob]:
    datasets_src_dir = [child for child in Path.iterdir(VIDEO_DIR) if child.is_dir()]
    extract_frames_jobs = {}
    for dataset_src_dir in datasets_src_dir:
        dataset_name = dataset_src_dir.stem
        dataset_out_dir = IMG_DIR / dataset_name
        extract_frames_jobs[dataset_name] = ExtractFramesJob(dataset_src_dir, dataset_out_dir)

    return extract_frames_jobs


if __name__ == "__main__":
    plac.call(main)
