"""Django settings for pytodo project."""
import os


def path(*args):
    """Path relative to OUR_ROOT."""
    return os.path.join(OUR_ROOT, *args)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Artemy Lebedev', 'tema@tema.ru'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'pytodo.db',
    }
}

TIME_ZONE = 'Antarctica/Vostok'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False
USE_L10N = False

OUR_ROOT = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = path('media')
MEDIA_URL = '/media/'

STATIC_ROOT = path('static')
STATIC_URL = '/static/'

SECRET_KEY = 'ou_$@t%3iq#$yjv5rbt__h8-(qvofcvr%=f34rf+u58l-7jy^2'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pytodo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pytodo.wsgi.application'

TEMPLATE_DIRS = [path('templates')]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Local apps
    'pytodo.main',
)
