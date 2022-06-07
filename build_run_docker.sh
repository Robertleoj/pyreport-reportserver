#!/bin/bash

docker rm -f report-server
docker build -t report-server .
docker run -d --name report-server -p 4000:80 --mount source=report_data,destination=/code/report_data report-server