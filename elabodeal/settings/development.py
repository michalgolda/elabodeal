from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elabodeal',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db',
        'PORT': 5432
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STRIPE_PUBLIC_API_KEY = config('STRIPE_PUBLIC_API_KEY', default=None)
STRIPE_API_KEY = config('STRIPE_API_KEY', default=None)
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET', default=None)