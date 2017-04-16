#!/bin/bash

set -eu

mkdir /tgcapp/logs
touch /tgcapp/logs/tgc.log
python setup.py install
python -m unittest discover -s /tgcapp/tgc
