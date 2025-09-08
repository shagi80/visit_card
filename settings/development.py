from .base import *
from .base import BASE_DIR, get_env_variable

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / get_env_variable('DB_NAME'),
    }
}
