#!/bin/bash

set -e
export PIP_USER=false

virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
deactivate