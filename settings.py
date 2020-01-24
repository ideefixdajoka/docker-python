"""
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd0dzwsfiy=gheo5^i59opiyed)_$8&zq$u(=ncbiqv49pw_so6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if 'DATABASE_HOST' in os.environ:
    DATABASES['default']['HOST'] = os.getenv('DATABASE_HOST')
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    DATABASES['default']['NAME'] = os.getenv('DATABASE_NAME')
    DATABASES['default']['USER'] = os.getenv('DATABASE_USER')
    DATABASES['default']['PASSWORD'] = os.getenv('DATABASE_PASSWORD')
