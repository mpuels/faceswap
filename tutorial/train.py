#!/usr/bin/env python3

import subprocess

import plac

from config import FACE_DIR, MODEL_DIR
from train_tasks import TRAIN_TASKS, TrainTask


@plac.annotations(
    train_task_name="Name of the training task. The special task 'list' lists "
                    "all tasks.",
    dry_run=("Don't actually run the training, instead just print the command "
             "and exist.",
             "flag")
)
def main(train_task_name, dry_run):
    """Run a training task

    A task consists of

        * name
        * face_a
        * face_b
        * train_args

    That translates to the following execution:

        python faceswap.py train -A ~/data/face/<face_a> -B ~/data/face/<face_b> -m ~/data/models/<name> <train_args>
    """
    if train_task_name == "list":
        for task_name in sorted(TRAIN_TASKS):
            print_train_task(task_name, TRAIN_TASKS[task_name])
        return 0

    if train_task_name not in TRAIN_TASKS:
        print(f"ERROR: Unknown task '{train_task_name}'. List all training "
              f"tasks with 'list'.")
        return 1

    task = TRAIN_TASKS[train_task_name]

    model_dir = MODEL_DIR / train_task_name

    cmd = ["python", "../faceswap.py", "train",
           "-A", str(FACE_DIR / task.face_a),
           "-B", str(FACE_DIR / task.face_b),
           "-m", str(model_dir)] + task.train_args

    if dry_run:
        print(cmd)
        return 0

    model_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd)


def print_train_task(task_name: str, train_task: TrainTask):
    print(task_name)
    print(f'    {train_task.face_a}')
    print(f'    {train_task.face_b}')
    for train_arg in train_task.train_args:
        print(f'    {train_arg}')


if __name__ == "__main__":
    plac.call(main)
