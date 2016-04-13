"""
Django settings for gente project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jx$tn(1r&6pjp+$-m13f+-on@uio0yi4c&w$k0nyoy)d(556%('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'genteai',
    'facebook_login',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gente.urls'

WSGI_APPLICATION = 'gente.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_URL = 'http://localhost:8000/'

ERROR_REDIRECT_URL = 'http://localhost:8000/accounts/login-user'

FACEBOOK_CLIENT_ID = '1726548184289137'
FACEBOOK_CLIENT_SECRET = '22acacf705312d37f1d326ad5973a4db'
FACEBOOK_REDIRECT_URL = 'facebook/authentication'
LOGIN_REDIRECT_URL = '/ai/'
LOGIN_URL = '/'
WEATHER_API_KEY = "ad2fbdb98b5d72a968053e7e8cab9e0b"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q=JInd&APPID=ad2fbdb98b5d72a968053e7e8cab9e0b"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )



STATIC_URL = '/static/'

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
