#!/bin/bash
docker build -t gitmeow . 
docker run --rm -p 50004:50004 -d --name gitmeow gitmeow 
