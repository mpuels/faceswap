#!/bin/bash

set -euo pipefail

DATA_DIR=~/data

CAGE_VIDEO_DIR=${DATA_DIR}/video/cage
CAGE_IMG_DIR=${DATA_DIR}/img/cage

mkdir -p ${CAGE_IMG_DIR}
ffmpeg -i ${CAGE_VIDEO_DIR}/cage-001.mp4 ${CAGE_IMG_DIR}/cage-001-%d.png
ffmpeg -i ${CAGE_VIDEO_DIR}/cage-002.mp4 ${CAGE_IMG_DIR}/cage-002-%d.png


TRUMP_VIDEO_DIR=${DATA_DIR}/video/trump
TRUMP_IMG_DIR=${DATA_DIR}/img/trump

mkdir -p ${TRUMP_IMG_DIR}
ffmpeg -i ${TRUMP_VIDEO_DIR}/trump-001.mp4 ${TRUMP_IMG_DIR}/trump-001-%d.png
