#!/usr/bin/env bash

DEPLOY_HOME="/srv/deploy/optrix"
NUM_WORKERS=4
WSGI_HOST="0.0.0.0"
WSGI_PORT="8000"
ERRLOG="$DEPLOY_HOME/logs/wsgi_server.err"
ACCESS_LOG="$DEPLOY_HOME/logs/wsgi_server.access"

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z db 5432 ; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#ls -la /srv/deploy/optrix/htdocs
cd $DEPLOY_HOME/db
#echo "Doing Migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collecting Static files..."
chown -R deploy:deploy /srv/deploy/optrix
#ls -la /srv/deploy/optrix/htdocs
python3 manage.py collectstatic --noinput
python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
chown -R deploy:deploy /srv/deploy/optrix/htdocs/static


exec gunicorn -w $NUM_WORKERS -b $WSGI_HOST:$WSGI_PORT --access-logfile $ACCESS_LOG --error-logfile $ERRLOG optrix.wsgi:application --preload --timeout 480