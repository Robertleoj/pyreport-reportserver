#!/bin/bash

docker build -t report-server .
docker run -d --name reportserver -p 4000:80 report-server