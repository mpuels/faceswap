#!/bin/bash

set -euo pipefail

pushd ..

python faceswap.py convert -i ~/data/img/trump -o ~/data/swaps/cage-for-trump/ -m ~/data/models/

popd
