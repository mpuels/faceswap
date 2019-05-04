from typing import NamedTuple

from config import IMG_DIR


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
        ]),
    "marcpuels-janboehmermann": TrainTask(
        "marcpuels",
        "janboehmermann",
        [
            "--trainer", "dfaker",
            "--warp-to-landmarks",
            "--alignments-A", str(IMG_DIR / "marcpuels" / "alignments.json"),
            "--alignments-B", str(IMG_DIR / "janboehmermann" / "alignments.json"),
            "--batch-size", "64",
            "--write-image",
        ]
    )
}
