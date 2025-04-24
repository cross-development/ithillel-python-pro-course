"""
Celery configuration for the application.

This module configures Celery for the project.
"""

import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')

app = Celery('hw_24')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(["celery_tasks"])

app.conf.beat_schedule = {
    'log-user-count-every-10-minutes': {
        'task': 'celery_tasks.tasks.log_user_count',
        'schedule': timedelta(minutes=10),
    },
}
