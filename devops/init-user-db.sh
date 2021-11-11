#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER $DJANGO_DB_USER WITH PASSWORD '$DJANGO_DB_PASSWORD';
    GRANT ALL PRIVILEGES ON DATABASE comic_server TO comic_psql_user;
EOSQL
