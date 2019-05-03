#!/bin/bash

set -euo pipefail

DATA_DIR=~/data
S3_BUCKET_NAME=gifswap-39485849

aws s3 sync ${DATA_DIR}/models s3://${S3_BUCKET_NAME}/models
