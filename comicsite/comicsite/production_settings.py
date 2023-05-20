from .common_settings import *
from decouple import config, Csv

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join('/var/backups/comic_server', 'db.sqlite3')
        },
        # 'postgres_default': {
        #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #     'NAME': config('DB_NAME'),
        #     'USER': config('DB_USER'),
        #     'PASSWORD': config('DB_PASSWORD'),
        #     'HOST': config('DB_HOST'),
        #     'PORT': '',
        #     }
        }

# directories for static files
ENV_PATH = '/var/www/static_files/'
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')
STATIC_ROOT = os.path.join(ENV_PATH, 'static/')

ANALYTICS_TRACKING_ID = 'G-B9YJ0J3QN4'

DBBACKUP_STORAGE_OPTIONS = {'location': '/var/backups/comic_server'}

# DBBACKUP_CONNECTORS = {
#     'default': {
    # Connector doesn't help much with restore
#         'CONNECTOR': 'dbbackup.db.postgresql.PgDumpBinaryConnector',
#     }
# }
