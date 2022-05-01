#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn framework.wsgi:application -w 4 -b 0.0.0.0:8000
