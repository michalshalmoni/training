# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'training.settings')

app = Celery('training')
app.config_from_object('django.conf:settings')
app.conf.ONCE = {
    'backend': 'celery_once.backends.Redis',
    'settings': {
        'url': settings.CELERY_REDIS_URL,
        'default_timeout': 60 * 60,
    },
}

#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)