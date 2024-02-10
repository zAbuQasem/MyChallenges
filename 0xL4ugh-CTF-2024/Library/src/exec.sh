#!/bin/sh

while true; do
    socat TCP-LISTEN:50003,reuseaddr,fork SYSTEM:'python3 challenge.py'
done
