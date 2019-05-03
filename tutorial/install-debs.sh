#!/bin/bash

set -euo pipefail

sudo apt install -y cmake ffmpeg

# Oddly we have to remove and re-install cmake. Otherwise the command 'cmake'
# is not available on the command line.
sudo apt remove -y cmake
sudo apt install -y cmake
