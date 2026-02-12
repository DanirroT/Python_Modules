#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install flake8
alias norminette=flake8
alias python=python3