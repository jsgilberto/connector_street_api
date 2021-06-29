#!/bin/bash

# Build
docker build \
    --file ./compose/production/traefik/Dockerfile \
    --tag "${REPOSITORY_URI}:latest" .

# Tag
docker tag "${REPOSITORY_URI}:latest" "${REPOSITORY_URI}:${IMAGE_TAG}"

# Push
docker push "${REPOSITORY_URI}:latest"
docker push "${REPOSITORY_URI}:${IMAGE_TAG}"
