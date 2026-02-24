import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ['DB_HOST']
password = os.environ['DB_PASSWORD']
secret_key = os.environ['DB_SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': host,
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
