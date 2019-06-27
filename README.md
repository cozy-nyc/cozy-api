# cozy.nyc backend


## Setup for local development

1. `touch .env` To create a environment file with the following:
```bash
DEBUG=true
SECRET_KEY=[KEY]
DJANGO_SETTINGS_MODULE=config.settings.local
ALLOWED_HOSTS=0.0.0.0,localhost,127.0.0.1
CORS_WHITELIST=http://0.0.0.0:3000
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

You have a few options when it comes to running a development server on your machine.
You can install all the required packages and services on your machine or you can
use Docker. _Using docker for local development might be easier to get going on your machine._

### Local Build
#### Requirements:
* Python 3.6 or higher
* Postgres


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
#### Requirements:
* Docker 3
* docker-compose



2. Add the following lines to your `.env` file to setup your
 postgres server.  
```bash
# Docker Postgres

POSTGRES_PASSWORD=[PASSWORD]
POSTGRES_USER=[USER]
POSTGRES_DB=[DATABASE]
```

3. run a local development server:
```sh
./bin/develop
```


To use any django commands use:
```sh
./bin/django [COMMAND]
```


## Join Our Discord

**Discord** - <https://discord.gg/3WSA2SG>
