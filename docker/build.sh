#!/bin/bash

if [ -z "$TAG" ]; then
  TAG=toxicity_$1:latest
fi

exec docker build -f Dockerfile -t $TAG --build-arg MODEL_DIR=$1 --build-arg ANNOTATION_TYPE=$2 ..
