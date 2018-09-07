#!/usr/bin/env bash

python3.7 manage.py makemigrations page && \
python3.7 manage.py makemigrations content && \
python3.7 manage.py makemigrations &&  \
python3.7 manage.py migrate && \
python3.7 manage.py runserver 0.0.0.0:8000 --settings core.settings.staging