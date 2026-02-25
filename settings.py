import os
from dotenv import load_dotenv

load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['PORT_NUMBER'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['USER_NAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['WEBSITE_SECRET_KEY']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
