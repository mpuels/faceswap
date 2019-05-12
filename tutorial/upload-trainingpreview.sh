#!/bin/bash

set -euo pipefail

. config.sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

NOW=$(date -u +%Y-%m-%d-%H-%M-%S)
aws s3 cp ${DIR}/../training_preview.jpg \
       s3://${S3_BUCKET_NAME}/training_previews/training_preview-${NOW}.jpg
