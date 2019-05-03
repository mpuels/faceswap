#!/usr/bin/env python3

import subprocess

import plac

from config import IMG_DIR, MODEL_DIR, SWAPS_DIR
from convert_tasks import CONVERT_TASKS


@plac.annotations(
    convert_task_name="Name of the convert task. The special task 'list' lists "
                      "all tasks.",
    dry_run=("Don't actually run the convert command. Instead print the "
             "command that would have been executed and exit.",
             "flag")
)
def main(convert_task_name, dry_run):
    if convert_task_name == "list":
        for task_name, task in CONVERT_TASKS.items():
            print(task_name, task)
        return 0

    if convert_task_name not in CONVERT_TASKS:
        print(f"ERROR: Unknown convert task '{convert_task_name}'. List all "
              f"convert tasks with 'list'.")
        return 1

    task = CONVERT_TASKS[convert_task_name]

    swaps_dir = SWAPS_DIR / convert_task_name

    cmd = ["python", "../faceswap.py", "convert",
           "-i", str(IMG_DIR / task.img_dir),
           "-o", str(swaps_dir),
           "-m", str(MODEL_DIR / task.model)] + task.convert_args

    if dry_run:
        print(cmd)
        return 0

    swaps_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd)


if __name__ == "__main__":
    plac.call(main)
