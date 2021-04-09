import my_settings
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = my_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pinterest_style',
        'USER': 'pinterest_style',
        'PASSWORD': 'abc135!!',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
