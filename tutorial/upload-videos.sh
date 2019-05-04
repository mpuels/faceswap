#!/bin/bash

set -euo pipefail

. config.sh

aws s3 sync ${DATA_DIR}/video s3://${S3_BUCKET_NAME}/video
