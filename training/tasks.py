from __future__ import absolute_import
from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab


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


# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")), ignore_result=True)
def add_to_scheduled_counter():
    try:
        from training.models import ScheduledCounter
        c, created = ScheduledCounter.objects.get_or_create(id=1, defaults={'value': 0})
        c.value = c.value + 1
        c.save()

    except Exception as e:
       log.error(str(e))

