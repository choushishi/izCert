#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

# Create a superuser for dev environmnet
export DJANGO_SUPERUSER_PASSWORD="adminpass"
python manage.py createsuperuser --noinput \
--username admin \
--email admin@izcert.com

exec "$@"