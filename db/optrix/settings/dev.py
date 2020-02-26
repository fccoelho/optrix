import os
import sys
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+=%r&tifrvtste5)88zzq#4#qsq5u$xu=ptuu)1xh)huy$$d&#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = 'manage.py' in sys.argv[0]


if DEBUG_WITH_RUNSERVER:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'app', 'build', 'static')
    ]


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # To enable GeoDjango:
        # 'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'conf', 'testproject.sqlite3'),
    }
}

# SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'
