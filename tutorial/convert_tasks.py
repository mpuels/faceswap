from typing import NamedTuple

from config import IMG_DIR, MODEL_DIR, VIDEO_DIR


class ConvertTask(NamedTuple):
    convert_args: list


# ffmpeg -i marcpuelssample-001.mpg -vf scale=-1:480 marcpuelssample-001-480.mpg

CONVERT_TASKS = {
    "marcpuels"                                 : ConvertTask(
        [
            "--input-dir", IMG_DIR / "marcpuels",
            "--alignments", IMG_DIR / "marcpuels" / "alignments.json",
            "--loglevel", "TRACE",
            "--model", MODEL_DIR / "marcpuels-janboehmermann",
            # "--singleprocess",
        ]),
    "marcpuels-distances-480"                   : ConvertTask(
        [
            '--input-dir', IMG_DIR / "marcpuels-distances-480",
            '--reference-video', VIDEO_DIR / "marcpuels-distances-480" / 'marcpuels-distances-480.mpg',
            '--alignments', IMG_DIR / "marcpuels-distances-480" / 'alignments.json',
            '--model', MODEL_DIR / "marcpuels-janboehmermann_villain",
            '--writer', 'ffmpeg'
        ]
    ),
    "marcpuels-distances-cut-1080"              : ConvertTask(
        [
            '--input-dir', IMG_DIR / "marcpuels-distances-cut-1080",
            '--reference-video', VIDEO_DIR / "marcpuels-distances-cut-1080" / 'marcpuels-distances-cut-1080.mp4',
            '--alignments', IMG_DIR / "marcpuels-distances-cut-1080" / 'alignments.json',
            '--model', MODEL_DIR / "marcpuels-janboehmermann_villain",
            '--writer', 'ffmpeg'
        ]
    ),
    "marcpuels-distances-cut-1080-clean"        : ConvertTask(
        [
            '--input-dir', IMG_DIR / "marcpuels-distances-cut-1080",
            '--reference-video', VIDEO_DIR / "marcpuels-distances-cut-1080" / 'marcpuels-distances-cut-1080.mp4',
            '--alignments', IMG_DIR / "marcpuels-distances-cut-1080" / 'alignments.json',
            '--model', MODEL_DIR / "marcpuels-janboehmermann_villain_fit_distance",
            '--writer', 'ffmpeg'
        ]
    ),
    "marcpuels-baseballcap-1080-cut"            : ConvertTask(
        [
            '--input-dir', IMG_DIR / "marcpuels-baseballcap-1080-cut",
            '--reference-video', VIDEO_DIR / "marcpuels-baseballcap-1080-cut" / 'marcpuels-baseballcap-1080-cut.mp4',
            '--alignments', IMG_DIR / "marcpuels-baseballcap-1080-cut" / 'alignments.json',
            '--model', MODEL_DIR / "marcpuels-janboehmermann_villain_fit_baseball",
            '--writer', 'ffmpeg'
        ]
    ),
    "marcpuels-baseballcap-1080-cut2"           : ConvertTask(
        [
            '--input-dir', IMG_DIR / "marcpuels-baseballcap-1080-cut2",
            '--reference-video', VIDEO_DIR / "marcpuels-baseballcap-1080-cut2" / 'marcpuels-baseballcap-1080-cut2.mp4',
            '--alignments', IMG_DIR / "marcpuels-baseballcap-1080-cut2" / 'alignments.json',
            '--model', MODEL_DIR / "marcpuels-janboehmermann_villain_fit_baseball",
            '--writer', 'ffmpeg'
        ]
    ),
    "marcpuels-baseballcap-1080-cut3"           : ConvertTask(
        [
            '--input-dir', IMG_DIR / "marcpuels-baseballcap-1080-cut3",
            '--reference-video', VIDEO_DIR / "marcpuels-baseballcap-1080-cut3" / 'marcpuels-baseballcap-1080-cut3.mp4',
            '--alignments', IMG_DIR / "marcpuels-baseballcap-1080-cut3" / 'alignments.json',
            '--model', MODEL_DIR / "marcpuels-janboehmermann_villain_fit_baseball3",
            '--writer', 'ffmpeg'
        ]
    ),
    "marcpuelssample-001-video"                 : ConvertTask(
        [
            "--input-dir", IMG_DIR / "marcpuels-sample",
            "--reference-video", VIDEO_DIR / "marcpuels-sample" / "marcpuelssample-001.mpg",
            "--model", MODEL_DIR / "marcpuels-janboehmermann_villain",
            "--writer", "ffmpeg",
        ]
    ),
    "marcpuelssample-002-video"                 : ConvertTask(
        [
            "--input-dir", IMG_DIR / "marcpuels-sample-002",
            "--reference-video", VIDEO_DIR / "marcpuels-sample-002" / "marcpuelssample-002.avi",
            "--model", MODEL_DIR / "marcpuels-janboehmermann_villain",
            "--writer", "ffmpeg",
        ]
    ),
    "marcpuels-sample-001-480"                  : ConvertTask(
        [
            '--input-dir', IMG_DIR / "marcpuels-sample-001-480",
            '--reference-video', VIDEO_DIR / "marcpuels-sample-001-480" / 'marcpuelssample-001-480.mpg',
            '--alignments', IMG_DIR / "marcpuels-sample-001-480" / 'alignments.json',
            '--model', MODEL_DIR / "marcpuels-janboehmermann_villain",
            '--writer', 'ffmpeg'
        ]
    ),
    "marcpuels_sample"                          : ConvertTask(
        [
            "--input-dir", IMG_DIR / "marcpuels_sample",
            "--model", MODEL_DIR / "marcpuels-janboehmermann",
            "--alignments", IMG_DIR / "marcpuels" / "alignments.json",
        ]
    ),
    "marcpuels-for-trumpsample"                 : ConvertTask(
        [
            "--input-dir", IMG_DIR / "trumpsample",
            "--model", MODEL_DIR / "trump-marcpuels",
        ]
    ),
    "marcpuels_nachricht_an_alex_sample"        : ConvertTask(
        [
            "--input-dir", IMG_DIR / "marcpuels_nachricht_an_alex_sample",
            "--model", MODEL_DIR / "marcpuels-janboehmermann",
            "--alignments", IMG_DIR / "marcpuels_nachricht_an_alex" / "alignments.json",
        ]
    ),
    "marcpuels_nachricht_an_alex_sample-villain": ConvertTask(
        [
            "--input-dir", IMG_DIR / "marcpuels_nachricht_an_alex_sample",
            "--model", MODEL_DIR / "marcpuels-janboehmermann_villain",
            "--alignments", IMG_DIR / "marcpuels_nachricht_an_alex" / "alignments.json",
        ]
    ),
    "marcpuels_nachricht_an_alex_sample_trump"  : ConvertTask(
        [
            "--input-dir", IMG_DIR / "marcpuels_nachricht_an_alex_sample",
            "--model", "rump-marcpuels",
            "--alignments", IMG_DIR / "marcpuels_nachricht_an_alex" / "alignments.json",
        ]
    )
}
