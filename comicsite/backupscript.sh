#!/bin/bash

DJANGO_SETTINGS_MODULE=comicsite.production_settings
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
python manage.py dbbackup --noinput --quiet --no-color --compress
python manage.py mediabackup --noinput --quiet --no-color --compress
