#!/usr/bin/env bash
# exit on error


poetry install

pip install -r requirements.txt
python manage.py migrate