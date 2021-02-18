#!/bin/sh

set -e

python manage.py collectstatic --noinput
echo "starting migrations"

uwsgi --socket :8000 --master --enable-threads --module serviceloader.wsgi
