@echo off

echo Building Docker image...
docker build -t password-generator-tests .

./docker_run.bat