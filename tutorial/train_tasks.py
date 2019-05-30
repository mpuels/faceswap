from typing import NamedTuple

from config import IMG_DIR


class TrainTask(NamedTuple):
    face_a: str
    face_b: str
    train_args: list


TRAIN_TASKS = {
    "trump-marcpuels"                               : TrainTask(
        "trump",
        "marcpuels",
        [
            "--batch-size", "128",
            "--write-image",
        ]),
    "marcpuels-janboehmermann"                      : TrainTask(
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
    ),
    "marcpuels-janboehmermann_villain"              : TrainTask(
        "marcpuels",
        "janboehmermann",
        [
            "--trainer", "villain",
            "--alignments-A", str(IMG_DIR / "marcpuels" / "alignments.json"),
            "--alignments-B", str(IMG_DIR / "janboehmermann" / "alignments.json"),
            "--batch-size", "8",
            "--write-image",
        ]
    ),
    "marcpuels-janboehmermann_villain_fit_distance" : TrainTask(
        "marcpuels-distances-cut-1080-clean",
        "janboehmermann",
        [
            "--trainer", "villain",
            "--alignments-A", str(IMG_DIR / "marcpuels-distances-cut-1080" / "alignments.json"),
            "--alignments-B", str(IMG_DIR / "janboehmermann" / "alignments.json"),
            "--batch-size", "8",
            "--write-image",
        ]
    ),
    "marcpuels-janboehmermann_villain_fit_baseball" : TrainTask(
        "marcpuels-baseballcap-1080-cut",
        "janboehmermann",
        [
            "--trainer", "villain",
            "--alignments-A", str(IMG_DIR / "marcpuels-baseballcap-1080-cut" / "alignments.json"),
            "--alignments-B", str(IMG_DIR / "janboehmermann" / "alignments.json"),
            "--batch-size", "8",
            "--write-image",
        ]
    ),
    "marcpuels-janboehmermann_villain_fit_baseball2": TrainTask(
        "marcpuels-baseballcap-1080-cut",
        "janboehmermann",
        [
            "--trainer", "villain",
            "--alignments-A", str(IMG_DIR / "marcpuels-baseballcap-1080-cut2" / "alignments.json"),
            "--alignments-B", str(IMG_DIR / "janboehmermann" / "alignments.json"),
            "--batch-size", "8",
            "--write-image",
        ]
    ),
    "marcpuels-janboehmermann_villain_fit_baseball3": TrainTask(
        "marcpuels-baseballcap-1080-cut3",
        "janboehmermann",
        [
            "--trainer", "villain",
            "--alignments-A", str(IMG_DIR / "marcpuels-baseballcap-1080-cut3" / "alignments.json"),
            "--alignments-B", str(IMG_DIR / "janboehmermann" / "alignments.json"),
            "--batch-size", "8",
            "--write-image",
        ]
    ),
}
