#!/bin/bash

echo "Building Docker image..."
docker build -t password-generator-tests .

./docker_run.sh