from .base import *


SECRET_KEY = 'im@-i-&3*(0(w46gjp%3770$8j+y%9cwzkrram)sb@_o^6(1@('

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

STRIPE_PUBLIC_API_KEY = config('STRIPE_PUBLIC_API_KEY', default=None)
STRIPE_API_KEY = config('STRIPE_API_KEY', default=None)
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET', default=None)