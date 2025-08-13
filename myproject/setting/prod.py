
from myproject.settings import *
from pathlib import Path
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b^i@(1u9!vlm_@t%8x@x_cu9=*8u1m$ohdowmal5juoh+j9d%1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['shahriyarshargh.ir','www.shahriyarshargh.ir']

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'captcha',
    'django_extensions',
    'robots',
    'debug_toolbar',
    'django_summernote',
    'taggit',
    'myapp',
    'pages',
    'blog_pages',
    'accounts',
]








SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'

X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SECURE = True