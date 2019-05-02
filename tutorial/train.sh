#!/bin/bash

set -euo pipefail

DATA_DIR=~/data

CAGE_FACE_DIR=${DATA_DIR}/face/cage
TRUMP_FACE_DIR=${DATA_DIR}/face/trump

MODEL_DIR=${DATA_DIR}/models

pushd ..

python faceswap.py train -A ${TRUMP_FACE_DIR} -B ${CAGE_FACE_DIR} -m ${MODEL_DIR}

popd
