#!/bin/bash

set -euo pipefail

. config.sh

aws s3 sync s3://${S3_BUCKET_NAME}/training_previews ${DATA_DIR}/training_previews
