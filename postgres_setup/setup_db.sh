#!/bin/bash
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE ROLE optrixadmin PASSWORD 'adminpass';
    CREATE DATABASE optrix WITH OWNER optrixadmin ENCODING 'utf-8';
    GRANT ALL PRIVILEGES ON DATABASE optrix to optrixadmin;
EOSQL