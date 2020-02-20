#!/bin/bash

DJANGO_SUPERUSER_PASSWORD="admin"

python manage.py migrate
python manage.py createsuperuser --email "jpolonia@evolutio.pt" --username "admin" --no-input
