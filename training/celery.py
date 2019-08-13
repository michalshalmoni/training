from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'training.settings')

app = Celery('training')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(settings, namespace='CELERY')

# this is ncessary for CELERY_ONCE To use REDIS URL
app.conf.update(
    CELERY_RESULT_BACKEND=settings.CELERY_RESULT_BACKEND,
    ONCE_REDIS_URL = settings.CELERY_BROKER_URL
)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    return "debug world"