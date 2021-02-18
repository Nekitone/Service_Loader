#!/bin/sh

set -e

python manage.py collectstatic --noinput
echo "starting migrations"
python manage.py makemigrations
python manage.py migrate importer

uwsgi --socket :8000 --master --enable-threads --module serviceloader.wsgi
