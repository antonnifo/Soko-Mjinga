import os
from .base import *

DEBUG = True

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD':os.getenv('DB_PASSWORD'),
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
}
# python manage.py runserver --settings=Engine.settings.local


import mimetypes

mimetypes.add_type('application/javascript', '.js', True)
mimetypes.add_type('text/css', '.css', True)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
# Google Client Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Stripe settings
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY') # Publishable key
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')      # Secret key
STRIPE_API_VERSION = os.getenv('STRIPE_API_VERSION')


STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')
