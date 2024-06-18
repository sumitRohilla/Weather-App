#!/bin/bash

echo "BUILD START"

# Install pip
apt-get update && apt-get install -y python3-pip

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
