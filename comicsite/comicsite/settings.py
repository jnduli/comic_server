import os
from .common_settings import *
from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES_AVAILABLE = {
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # created to help test out backups and run full website locally
    'server': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', None),
        'PORT': '',
        }
}

database = os.environ.get('DJANGO_DATABASE', 'test')
DATABASES = {
    'default': DATABASES_AVAILABLE[database]
}

# directories for static files
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')
STATIC_ROOT = os.path.join(ENV_PATH, 'static/')

ANALYTICS_TRACKING_ID = ''

# DBBACKUP_CONNECTORS = {
#     'default': {
#         'CONNECTOR': 'dbbackup.db.postgresql.PgDumpBinaryConnector',
#     }
# }

DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR,'backups/')}
