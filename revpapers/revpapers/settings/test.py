from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
        'USER': '',
        'PASSWORD': '',
        'HOST':'',
        'PORT':'',
    }
}

# TODO add django-coverage to apps
# TODO add django-discover-runner to apps
# TODO add django-webtest to apps
