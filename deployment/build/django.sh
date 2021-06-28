#!/bin/bash

# Build
docker build \
    --build-arg DJANGO_SETTINGS_MODULE \
    --build-arg DJANGO_SECRET_KEY \
    --build-arg DJANGO_ADMIN_URL \
    --build-arg DJANGO_ALLOWED_HOSTS \
    --build-arg DJANGO_SECURE_SSL_REDIRECT \
    --build-arg DJANGO_SERVER_EMAIL \
    --build-arg DJANGO_AWS_ACCESS_KEY_ID \
    --build-arg DJANGO_AWS_SECRET_ACCESS_KEY \
    --build-arg DJANGO_AWS_STORAGE_BUCKET_NAME \
    --build-arg DJANGO_AWS_ACCESS_KEY_FOR_ANYMAIL_SES \
    --build-arg DJANGO_AWS_SECRET_KEY_FOR_ANYMAIL_SES \
    --build-arg DJANGO_ACCOUNT_ALLOW_REGISTRATION \
    --build-arg WEB_CONCURRENCY \
    --build-arg REDIS_URL \
    --build-arg CELERY_FLOWER_USER \
    --build-arg CELERY_FLOWER_PASSWORD \
    --build-arg DATABASE_URL \
    --build-arg CELERY_BROKER_URL \
    --build-arg POSTGRES_HOST \
    --build-arg POSTGRES_PORT \
    --build-arg POSTGRES_DB \
    --build-arg POSTGRES_USER \
    --build-arg POSTGRES_PASSWORD \
    --file ./compose/production/django/Dockerfile \
    --tag $REPOSITORY_URI:latest .

# Tag
docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG

# Push
docker push $REPOSITORY_URI:latest
docker push $REPOSITORY_URI:IMAGE_TAG
