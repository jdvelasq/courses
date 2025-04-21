#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

pip3 install --quiet --upgrade pip
pip3 install --quiet -r requirements.txt


