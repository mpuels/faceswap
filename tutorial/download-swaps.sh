#!/bin/bash

set -euo pipefail

. config.sh

aws s3 sync s3://${S3_BUCKET_NAME}/swaps ${DATA_DIR}/swaps
