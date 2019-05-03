#!/bin/bash

set -euo pipefail

. config.sh

NAME_A=trump
NAME_B=marcpuels

MODEL_DIR=${DATA_DIR}/models/${NAME_A}-${NAME_B}

pushd ..

python faceswap.py train \
       --batch-size 128 \
       -L TRACE \
       -A ${DATA_DIR}/face/${NAME_A} \
       -B ${DATA_DIR}/face/${NAME_B} \
       -m ${MODEL_DIR}

popd
