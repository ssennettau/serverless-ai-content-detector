#!/bin/bash

mkdir ~/mount

sudo mount -t nfs -o rw [EFS-EndPoint]:/ ~/mount

python -m pip install -r req-pytorch.txt -t ~/mount/lambda/packages --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r req-std.txt -t ~/mount/lambda/packages

ls ~/mount/lambda/packages