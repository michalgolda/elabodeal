import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elabodeal.settings.development')

app = Celery('elabodeal')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()