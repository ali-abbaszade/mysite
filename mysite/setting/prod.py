from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iw*lpb^ife@4nox_(lx68272)oqnqi3)$gsxys(wz-uu^@yksh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Sites Framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ali_travel',
        'USER': 'dbadmin',
        'PASSWORD': '###',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# X-Frame-Options
X_FRAME_OPTIONS = 'DENY'

#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True

# Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# that requests over HTTP are redirected to HTTPS
SECURE_SSL_REDIRECT = True 

# X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'