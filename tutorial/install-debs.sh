#!/bin/bash

set -euo pipefail

sudo apt install cmake ffmpeg

# Oddly we have to remove and re-install cmake. Otherwise the command 'cmake'
# is not available on the command line.
sudo apt remove cmake
sudo apt install cmake
