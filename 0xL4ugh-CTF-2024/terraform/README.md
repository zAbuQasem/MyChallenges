# TerraMeow [Easy]
## Description
An easy challenge to get you to learn the basics of IAC with Terraform.

> Author: zAbuQasem

## Solution
Each of the following payloads could be used to solve the challenge:
```
base64encode(file("terraform.tfstate"))
base64encode(local_file.flag.filename)
strrev(var.FLAG)
```
