#Settings for NFL Week Application

import os
from env import env
from os.path import join
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    join(BASE_DIR, 'NFL_App/media/_template'),
)

STATICFILES_DIRS = (
    join(BASE_DIR, 'static_dev'),
)

SECRET_KEY = env.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Permission redirection
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = ''

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

Django_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

Local_APPS = (
    'Select',
    'User',
)

Third_Party_APPS = (
    'gunicorn',
)

INSTALLED_APPS = Django_APPS + Local_APPS + Third_Party_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'NFL_App.urls'

WSGI_APPLICATION = 'NFL_App.wsgi.application'

AUTHENTICATION_BACKENDS = ('NFL_App.backends.NFLCaseInsensitiveLogin',)

DATABASES = {
    'default': {
    'ENGINE' : 'django.db.backends.postgresql_psycopg2',
    'NAME' : env.get('DB_NAME'),
    'USER' : env.get('DB_USER'),
    'PASSWORD' : env.get('DB_PASSWORD'),
    'HOST' : 'localhost',
    'PORT' : '',
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
