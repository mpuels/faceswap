from typing import NamedTuple


class TrainTask(NamedTuple):
    face_a: str
    face_b: str
    train_args: list


TRAIN_TASKS = {
    "trump-marcpuels": TrainTask(
        "trump",
        "marcpuels",
        [
            "--batch-size", "128",
            "--write-image",
        ])
}
