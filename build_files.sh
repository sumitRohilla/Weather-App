#!/bin/bash

echo "BUILD START"

# Install dependencies
python3.12.4 -m pip install -r requirements.txt

# Collect static files
python3.12.4 manage.py collectstatic --noinput --clear

echo "BUILD END"
