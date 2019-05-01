#!/bin/bash

set -euo pipefail

pushd ..

PYTHON=venv/bin/python
DATA_DIR=~/data

CAGE_IMG_DIR=${DATA_DIR}/img/cage
CAGE_FACE_DIR=${DATA_DIR}/face/cage

mkdir -p ${CAGE_FACE_DIR}
${PYTHON} faceswap.py extract -i ${CAGE_IMG_DIR} -o ${CAGE_FACE_DIR}

TRUMP_IMG_DIR=${DATA_DIR}/img/trump
TRUMP_FACE_DIR=${DATA_DIR}/face/trump

mkdir -p ${TRUMP_FACE_DIR}
${PYTHON} faceswap.py extract -i ${TRUMP_IMG_DIR} -o ${TRUMP_FACE_DIR}

popd
