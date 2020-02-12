#!/bin/sh

set -e
. venv/bin/activate
echo "Starting Django..."
db/manage.py runserver &

