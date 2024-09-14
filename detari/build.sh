#!/usr/bin/env bash

set -o errexit

pip install -r detari/requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --no-input