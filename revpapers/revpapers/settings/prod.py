from .base import *

# to be filled out later

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '', # use dj-database-url
        'USER': '', # use env
        'PASSWORD': '', # use env
        'HOST': '',
        'PORT': '',
    }
}
