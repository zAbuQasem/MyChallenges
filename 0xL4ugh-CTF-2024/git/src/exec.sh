#!/bin/bash

# General configs
git config --global --add safe.directory /tmp
git config --global user.email "zAbuQasem@0xL4ugh.com"
git config --global user.name "zAbuQasem"

# Adding alot of files
i=1

while [ "$i" -le 1000 ]; do
  echo '0xL4ugh{f4k3_fl4g_f0r_n00b5}' > /tmp/$(head -n 10 /dev/urandom | md5sum | cut -d ' ' -f1).txt
  i=$((i + 1))
done

while true; do
    socat TCP-LISTEN:50004,reuseaddr,fork SYSTEM:'sh entrypoint.sh'
done
