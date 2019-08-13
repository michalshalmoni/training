from __future__ import absolute_import
from celery import shared_task, app
from celery_once import QueueOnce

import os

import logging
from celery.decorators import task
log = logging.getLogger(__name__)


@shared_task(base=QueueOnce)
def add_to_counter():
    try:
        from training.models import Counter
        c = Counter.objects.get(id=1)
        c.value = c.value + 1
        c.save()
        return c
    except Exception as e:
       log.error(str(e))


