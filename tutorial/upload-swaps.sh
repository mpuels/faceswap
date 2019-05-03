#!/bin/bash

set -euo pipefail

. config.sh

aws s3 sync ${DATA_DIR}/swaps s3://${S3_BUCKET_NAME}/swaps
