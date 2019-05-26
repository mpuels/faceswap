#!/bin/bash

set -euo pipefail

. config.sh

aws s3 sync --exclude '*' --include '*/alignments.json' ${DATA_DIR}/img s3://${S3_BUCKET_NAME}/img
