#!/bin/bash

set -euo pipefail

pushd ..

. config.sh

FACE_TO_REPLACE=trumpsample
FACE_TO_INSERT=marcpuels2

MODEL=trump-marcpuels

python faceswap.py convert \
       -i ${DATA_DIR}/img/${FACE_TO_REPLACE} \
       -o ${DATA_DIR}/swaps/${FACE_TO_INSERT}-for-${FACE_TO_REPLACE}/ \
       -m ${DATA_DIR}/models/${MODEL}

popd
