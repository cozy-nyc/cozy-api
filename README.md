# cozy.nyc backend
[![Build Status](https://travis-ci.org/cozy-nyc/cozy-nyc-backend.svg?branch=master&style=flat-square)](https://travis-ci.org/cozy-nyc/cozy-nyc-backend)

### Join Our Discord
__Discord__ - https://discord.gg/3WSA2SG

## Requirements
* Python 3.5 or higher

## Setup and customize

1. ` touch .env` To create a environement file with the following values filled

```
DEBUG=true
SECRET_KEY=[secret-key]
DJANGO_SETTINGS_MODULE=django_config.settings.local
ALLOWED_HOSTS=localhost,127.0.0.1, 0.0.0.0
DATABASE_URL=postgres://[user]:[password]@[ip or localhost]:5432/[database]

MAILGUN_API_KEY=[mailgun-api-key]
MAILGUN_DEFAULT_FROM_EMAIL=[email]

POSTGRES_PASSWORD=[password]
POSTGRES_USER=[user]
POSTGRES_DB=[database]

EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST=smtp.domain.com
EMAIL_HOST_USER=[email]
EMAIL_HOST_PASSWORD=[password]
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
DEFAULT_FROM_EMAIL=[default email]
```

2. In the requirements folder run
```
pip install -r local.txt
```

3. Run basic django commands such as
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
These steps should allow you to run the application no problem.
