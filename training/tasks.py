from __future__ import absolute_import
from celery import app
from celery.decorators import task


import logging
log = logging.getLogger(__name__)


@app.task(bind=True)
def add_to_counter():
    try:
        from training.models import Counter
        c = Counter.objects.get(id=1)
        c.value = c.value + 1
        c.save()
        return c
    except Exception as e:
       log.error(str(e))


