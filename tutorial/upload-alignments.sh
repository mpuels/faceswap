#!/bin/bash

set -euo pipefail

. config.sh

aws s3 sync --exclude '*' --include '*/alignments.json' ${DATA_DIR}/face s3://${S3_BUCKET_NAME}/face
