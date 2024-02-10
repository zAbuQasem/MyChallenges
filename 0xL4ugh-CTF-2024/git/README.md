# GitMeow [Medium]
## Description
Just another annoying git challenge :)

> Author: zAbuQasem


## Solution
The main idea of this challenge is to get the contestants to learn new git commands the hard way. The following payloads were the intended solution for the challenge:
```sh
-C /tmp init
-C /tmp add .
-C /tmp commit -m meow
# Listing files and pointing out the file with the different size
-C /tmp ls-tree -r -l master
# This file should contain the flag
-C /tmp show cadd234e166870f23bcdcd4cb494341f.txt
```
## Cool unintended
@cygnusx
```
update-ref -d refs/notes/commits
notes append -F /fla[g-g].txt
log
```
@hyperdrox
```
-C /tmp init
-C /tmp add .
-C /tmp commit -m test
-C /tmp show -I k3_fl
```
