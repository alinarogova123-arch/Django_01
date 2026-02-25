import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ['DB_HOST']
password = os.environ['DB_PASSWORD']
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

SECRET_KEY = os.environ['WEBSITE_SECRET_KEY']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True


