# Soko-Mjinga [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 
A Fully Featured Django  E-commerce Platform. 

## Features
1. Browse Products.
2. Product Recommendation Engine. 
3. Add Products to a Shopping Cart. 
4. Apply Coupon Codes.  
5. Checkout Process.
6. Pay with Credit card or M-pesa. 
7. Generate Invoices. 
8. Manage Customer Orders. 
9. Use of Multiple langaunges. 

## Getting Started. 
### Tech/Framework and Tools  
- Python, Django, Javascript, Bootstrap5.  
- Celery, RabbitMQ, Flower, Docker, Redis, PostgreSQL

### Installation. 
1. Get clone the app.  
`git@github.com:antonnifo/Soko-Mjinga.git`  

2. Create a Virtual Environment and activate it.  

``` 
python3 -m venv ./venv 
source venv/bin/activate 
```
3. Install Python Dependancies.  
`pip install -r requirements.txt`
4. Configure your settings.py file with the following data (Contents of local_settings.py)

```
DEBUG = True
ALLOWED_HOSTS = []

SECRET_KEY = 'A secret key'


ADMINS = (
            ('Name', 'your email')
)

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'DATABASE NAME',
                'USER': 'DATABASE USER',
                'PASSWORD':'USER PASSWORD',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
}

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

else:    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
    EMAIL_HOST = "MAIL SERVER"
    EMAIL_HOST_USER = "EMAIL"
    EMAIL_HOST_PASSWORD = "EMAIL PASSOWRD"
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True 

# Google Client ID
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXX'  
# Google Client Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXX'

# Stripe settings
STRIPE_PUBLISHABLE_KEY = 'XXX' # Publishable key
STRIPE_SECRET_KEY = 'XXX'      # Secret key
STRIPE_API_VERSION = '2022-08-01'


STRIPE_WEBHOOK_SECRET = 'XXX'. 
```

5. Apply. database migrations. 
`python manage.py migrate` 
6. Start local test server  
`python manage.py runserver` 
7. Installing & starting RAbbitMQ  
```
docker pull rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```
Access RabbitMQ's management via. 
`http://127.0.0.1:15672`. 
Username:guest. 
password:guest.  

8. Start Celery Worker process with the following command. 
`celery -A Engine worker -l info`.   

9. monitor celery with. flower using the command. 
`celery -A Engine flower`.   

Access flower dashboard via `http://localhost:5555/dashboard`. 
### Testing the app. 
- Create a super user and add a few products on the admin panel.
- Browser the shop and add a few products to cart and checkout.
- Use the following cards to simulate different payment scenarios.  
  
  
 
`Test Credit Cards `         
   | Result | Test Credit Card |  CVC | Expiry Date
| ----------- | ----------- | ------- | ---------- |
| Successful Payment | `4242 4242 4242 4242` | Any 3 digits | Any future date |
| Failed Payment | `4000 0000 0000 0002` | Any 3 digits | Any future date |
| Requires 3D secure authentication | `4000 0025 0000 3155` | Any 3 digits | Any future date |
