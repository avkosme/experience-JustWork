#!/usr/bin/env bash

rm -f /tmp/celerywork.pid && \
celery -A tasks.queue worker --loglevel=debug