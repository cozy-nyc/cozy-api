# cozy.nyc backend

### Join Our Discord
__Discord__ - https://discord.gg/3WSA2SG

## Requirements
* Python 3.6 or higher
* Postgres

## Setup for local development

1. `touch .env` To create a environment file with the following:
```bash
DEBUG=true
SECRET_KEY=[KEY]
DJANGO_SETTINGS_MODULE=config.settings.local
ALLOWED_HOSTS=0.0.0.0
CORS_WHITELIST=['https://0.0.0.0:3000']
DATABASE_URL=postgres://[user]:[password]@[ip or localhost]:5432/[database]

MAILGUN_API_KEY=[API_KEY]
MAILGUN_DEFAULT_FROM_EMAIL=[EMAIL]

EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST=smtp.domain.com
EMAIL_HOST_USER=[EMAIL]
EMAIL_HOST_PASSWORD=[PASSWORD]
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
DEFAULT_FROM_EMAIL=[DEFAULT_EMAIL]
```

2. Install required python packages:
```sh
pip3 install -r requirements/local.txt
```

3. Start up django:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


### Docker
Using docker for local development might be easier to get going on your machine.

We are using Docker 3 for this build.

1. Add the following lines to your `.env` file to setup your
 postgres server.  
```bash
# Docker Postgres

POSTGRES_PASSWORD=[PASSWORD]
POSTGRES_USER=[USER]
POSTGRES_DB=[DATABASE]
```

2. run a local development server:
```sh
./bin/develop
```


To use any django commands use:
```sh
./bin/django [COMMAND]
```
