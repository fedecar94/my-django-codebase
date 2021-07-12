# My codebase

_Read this in other languages: [English](README.md), [Español](README.es.md)._

I have done this project to save the initial work hours that a typical django project requires.

It is designed to be dockerized and it is very important that you load the environment variables according to your need

## This project has

- Rest API with auto-generated documentation using swagger
- Coroutines using Celery and Redis
- Uvicorn is used to be able to use asynchronous views
- It is ready to work with database replicas
- By default it is configured to use PostgreSQL
- For development use WhiteNoise, for production it is recommended that you use a CDN

## For development

1. sh scripts/pre-commit.sh
1. docker-compose build
1. docker-compose up django
1. (in another terminal) docker-compose exec django bash
1. python manage.py migrate
1. python manage.py createsuperuser
1. docker-compose stop
1. docker-compose up django beat worker flower (remember to restart beat and worker when creating new celery tasks, they do not restart automatically)

## For production

1. export COMPOSE_FILE=prod/docker-compose.yml
1. docker-compose build
1. docker tag codebase_django: latest < name of the registry where you want to upload >
1. docker push < name of the registry where you want to upload >
