from typing import NamedTuple

from config import IMG_DIR


class ConvertTask(NamedTuple):
    img_dir: str
    model: str
    convert_args: list


CONVERT_TASKS = {
    "marcpuels": ConvertTask(
        "marcpuels",
        "marcpuels-janboehmermann",
        [
            "--alignments", str(IMG_DIR / "marcpuels" / "alignments.json"),
            "--loglevel", "TRACE",
            # "--singleprocess",
        ]
    ),
    "marcpuels_sample": ConvertTask(
        "marcpuels_sample",
        "marcpuels-janboehmermann",
        [
            "--alignments", str(IMG_DIR / "marcpuels" / "alignments.json"),
            "--loglevel", "TRACE",
            # "--singleprocess",
        ]
    ),
    "marcpuels-for-trumpsample": ConvertTask(
        "trumpsample",
        "trump-marcpuels",
        []),
    "marcpuels_nachricht_an_alex_sample": ConvertTask(
        "marcpuels_nachricht_an_alex_sample",
        "marcpuels-janboehmermann",
        [
            # "--alignments", str(IMG_DIR / "marcpuels_nachricht_an_alex" / "alignments.json"),
            # "--swap-model",
            "--loglevel", "TRACE",
            "--singleprocess",
        ]),
    "marcpuels_nachricht_an_alex_sample_trump": ConvertTask(
        "marcpuels_nachricht_an_alex_sample",
        "trump-marcpuels",
        [
            # "--alignments", str(IMG_DIR / "marcpuels_nachricht_an_alex" / "alignments.json"),
            # "--swap-model",
            "--loglevel", "TRACE",
            "--singleprocess",
        ]),
}
