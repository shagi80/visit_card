from .base import *
from .base import get_env_variable


DEBUG = False

ALLOWED_HOSTS = ['svshaginyan.store', 'svshaginyan.ru']

DATABASES = {
    'default': {
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': get_env_variable('DB_PORT'),
        'POOL_OPTIONS': {
            'POOL_SIZE': 5,
            'MAX_OVERFLOW': 10,
            'TIMEOUT': 30,
            'RECYCLE': 1800,
        }
    }
}

# Security settings

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
