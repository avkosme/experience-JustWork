#!/usr/bin/env bash

pip3.6 install -r core/requirements/base.txt && \
python3.6 manage.py makemigrations page && \
python3.6 manage.py makemigrations content && \
python3.6 manage.py makemigrations &&  \
python3.6 manage.py migrate && \
python3.6 manage.py runserver 0.0.0.0:8000 --settings core.settings.staging