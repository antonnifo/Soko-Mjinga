from .base import *
import os


DEBUG = False

ADMINS = (
            ('Anthony ', os.getenv('EMAIL_HOST_USER'))
)

ALLOWED_HOSTS = ['sokomjinga.com', 'www.sokomjinga.com']

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.getenv('POSTGRES_DB'),
                'USER': os.getenv('POSTGRES_USER'),
                'PASSWORD':os.getenv('POSTGRES_PASSWORD'),
                'HOST': 'db',
                'PORT': '5432',
            }
}

# Email Settings 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 465
EMAIL_USE_SSL = True 

REDIS_URL = 'redis://cache:6379'

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True