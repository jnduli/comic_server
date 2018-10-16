#!/bin/bash

DJANGO_SETTINGS_MODULE=comicsite.production_settings
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
python manage.py dbbackup --compress
python manage.py mediabackup
