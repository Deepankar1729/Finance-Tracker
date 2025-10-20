#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py tailwind install
python manage.py tailwind build

python manage.py migrate --noinput
python manage.py collectstatic --noinput
