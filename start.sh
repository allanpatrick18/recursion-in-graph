#!/bin/sh
docker stop test-graph
echo "stop container"
docker rm test-graph
echo "remove container"
docker build -t  test-graph .
docker run -d --name=test-graph -p 9997:8080  test-graph
