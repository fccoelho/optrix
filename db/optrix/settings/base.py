"""
Django settings for optrix project.

Based on the Django 2.0 template, with wq-specific modifications noted as such.
Generated by 'wq start' 1.2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/

For more information about wq.db's Django settings see
http://wq.io/docs/settings

"""

import os
from os.path import dirname

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# wq: extra dirname()s to account for db/ and settings/ folders
BASE_DIR = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))

# wq: SECRET_KEY, DEBUG, and ALLOWED_HOSTS are defined in dev.py/prod.py


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.gis',
    'rest_framework',
    'wq.db.rest',
    'wq.db.rest.auth',

    # Project apps
    'optrix'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'optrix.urls'

# wq: Recommended settings for Django and rest_framework
from wq.db.default_settings import (
    TEMPLATES,
    SESSION_COOKIE_HTTPONLY,
    REST_FRAMEWORK,
)
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates')]

# wq: Recommended settings unique to wq.db
from wq.db.default_settings import (
    ANONYMOUS_PERMISSIONS,
    SRID,
)

WSGI_APPLICATION = 'optrix.wsgi.application'


# wq: DATABASES is defined in dev.py/prod.py

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# wq: Configure paths for default project layout
STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
VERSION_TXT = os.path.join(BASE_DIR, 'version.txt')
MEDIA_URL = '/media/'

SECURE_CONTENT_TYPE_NOSNIFF = False