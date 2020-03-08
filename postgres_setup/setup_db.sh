#!/bin/bash
#echo -e "\nhost all all all peer\nhost all all 127.0.0.1/32 md5" >> "$PGDATA/pg_hba.conf"
echo "===> Done editing pg_hba.conf"
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER"  <<-EOSQL
    CREATE USER $DJANGO_SUPERUSER_USERNAME SUPERUSER PASSWORD '$DJANGO_SUPERUSER_PASSWORD';
    CREATE DATABASE optrix WITH OWNER $DJANGO_SUPERUSER_USERNAME ENCODING 'utf-8';
    GRANT ALL PRIVILEGES ON DATABASE optrix to $DJANGO_SUPERUSER_USERNAME;
EOSQL