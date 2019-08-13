from __future__ import absolute_import
from celery import shared_task


import logging
log = logging.getLogger(__name__)

@shared_task
def add_to_counter():
    try:
        from training.models import Counter
        c = Counter.objects.get(id=1)
        c.value = c.value + 1
        c.save()

    except Exception as e:
       log.error(str(e))


@shared_task
def add_to_scheduled_counter():
    try:
        from training.models import ScheduledCounter
        c = ScheduledCounter.objects.get(id=1)
        c.value = c.value + 1
        c.save()

    except Exception as e:
       log.error(str(e))

