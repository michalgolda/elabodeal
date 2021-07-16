from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elabodeal',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'postgres',
        'PORT': 5432
    }
}

CELERY_BROKER_URL = 'redis://redis'

EMAIL_HOST = 'maildev'
DEFAULT_FROM_EMAIL = 'system@elabodeal.com'

STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY', default=None)
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', default=None)
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET', default=None)

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'