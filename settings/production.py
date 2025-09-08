from .base import *
from .base import BASE_DIR, get_env_variable


DEBUG = True

ALLOWED_HOSTS = ['shagi80.beget.tech', 'svshaginyan.store', 'svshaginyan.ru' ]

DATABASES = {
    'default': {
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': 'shagi80_vscard',
        'USER': 'shagi80_vscard',
        'PASSWORD': 'Shrtyjk_8006',
        'HOST': 'localhost',
        'PORT': '3306',
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