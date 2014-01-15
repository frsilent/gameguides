"""Demo settings and globals."""

from os import environ
from base import *
from django.core.exceptions import ImproperlyConfigured


DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gameguides',
        'USER': 'opensorcerer',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    }
}

TEMPLATE_DEBUG = DEBUG
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
