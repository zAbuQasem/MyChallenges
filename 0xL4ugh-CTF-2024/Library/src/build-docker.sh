#!/bin/bash
docker build -t noname .
docker run -p 50003:50003 --rm -it noname
