#!/bin/bash

set -euo pipefail

. config.sh

aws s3 cp ../training_preview.jpg s3://${S3_BUCKET_NAME}/training_preview.jpg
