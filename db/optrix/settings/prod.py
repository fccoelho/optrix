from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+=%r&tifrvtste5)88zzq#4#qsq5u$xu=ptuu)1xh)huy$$d&#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = False

ALLOWED_HOSTS = ["testproject.example.org"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres',
        # To enable GeoDjango:
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'testproject',
        'USER': 'testproject',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
