ARG PYTHON_VERSION=3.9-slim-buster



# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

# Python build stage
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=production

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt


# Python 'run' stage
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN addgroup --system django \
    && adduser --system --ingroup django django


# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/


COPY --chown=django:django ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY --chown=django:django ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
COPY --chown=django:django ./compose/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker


COPY --chown=django:django ./compose/production/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat


COPY ./compose/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


# copy application code to WORKDIR
COPY --chown=django:django . ${APP_HOME}

# make django owner of the WORKDIR directory as well.
RUN chown django:django ${APP_HOME}

USER django

# environment variables
ARG DJANGO_SETTINGS_MODULE
ARG DJANGO_SECRET_KEY
ARG DJANGO_ADMIN_URL
ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECURE_SSL_REDIRECT
ARG DJANGO_SERVER_EMAIL
ARG DJANGO_AWS_ACCESS_KEY_ID
ARG DJANGO_AWS_SECRET_ACCESS_KEY
ARG DJANGO_AWS_STORAGE_BUCKET_NAME
ARG DJANGO_AWS_ACCESS_KEY_FOR_ANYMAIL_SES
ARG DJANGO_AWS_SECRET_KEY_FOR_ANYMAIL_SES
ARG DJANGO_ACCOUNT_ALLOW_REGISTRATION
ARG WEB_CONCURRENCY
ARG REDIS_URL
ARG CELERY_FLOWER_USER
ARG CELERY_FLOWER_PASSWORD
ARG DATABASE_URL
ARG CELERY_BROKER_URL
ARG POSTGRES_HOST
ARG POSTGRES_PORT
ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

ENV DJANGO_SETTINGS_MODULE=DJANGO_SETTINGS_MODULE
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV DJANGO_ADMIN_URL=$DJANGO_ADMIN_URL
ENV DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS
ENV DJANGO_SECURE_SSL_REDIRECT=$DJANGO_SECURE_SSL_REDIRECT
ENV DJANGO_SERVER_EMAIL=$DJANGO_SERVER_EMAIL
ENV DJANGO_AWS_ACCESS_KEY_ID=$DJANGO_AWS_ACCESS_KEY_ID
ENV DJANGO_AWS_SECRET_ACCESS_KEY=$DJANGO_AWS_SECRET_ACCESS_KEY
ENV DJANGO_AWS_STORAGE_BUCKET_NAME=$DJANGO_AWS_STORAGE_BUCKET_NAME
ENV DJANGO_AWS_ACCESS_KEY_FOR_ANYMAIL_SES=$DJANGO_AWS_ACCESS_KEY_FOR_ANYMAIL_SES
ENV DJANGO_AWS_SECRET_KEY_FOR_ANYMAIL_SES=$DJANGO_AWS_SECRET_KEY_FOR_ANYMAIL_SES
ENV DJANGO_ACCOUNT_ALLOW_REGISTRATION=$DJANGO_ACCOUNT_ALLOW_REGISTRATION
ENV WEB_CONCURRENCY=$WEB_CONCURRENCY
ENV REDIS_URL=$REDIS_URL
ENV CELERY_FLOWER_USER=$CELERY_FLOWER_USER
ENV CELERY_FLOWER_PASSWORD=$CELERY_FLOWER_PASSWORD
ENV DATABASE_URL=$DATABASE_URL
ENV CELERY_BROKER_URL=$CELERY_BROKER_URL
ENV POSTGRES_HOST=$POSTGRES_HOST
ENV POSTGRES_PORT=$POSTGRES_PORT
ENV POSTGRES_DB=$POSTGRES_DB
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

ENTRYPOINT ["/entrypoint"]
