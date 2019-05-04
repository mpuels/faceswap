#!/bin/bash

set -euo pipefail

. config.sh

aws s3 cp s3://${S3_BUCKET_NAME}/training_preview.jpg ${DATA_DIR}/training_preview.jpg
