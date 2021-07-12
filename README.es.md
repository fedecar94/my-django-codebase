# Mi codigo base

_Lee esto en otro lenguaje: [English](README.md), [Español](README.es.md)._

Este proyecto lo he realizado para ahorrarme las horas de trabajo inicial que requiere un proyecto tipico de django

Está pensado para se dockerizado y es muy importante que cargues las variables de entorno segun tu necesidad

## Este proyecto cuenta con

- API Rest con documentación autogenerada usando swagger
- Corutinas utilizando [Celery](https://docs.celeryproject.org/en/stable/) y [Redis](https://redis.io/)
- Se utliza [Uvicorn](https://www.uvicorn.org) para poder utilizar vistas asincronas
- Está preparado para trabajar con replicas de bases de datos
- Por defecto está configurado para usar [PostgreSQL](https://www.postgresql.org)
- Para desarrollo utiliza [WhiteNoise](https://whitenoise.evans.io/en/stable/), para producción es recomendable que utilizes una CDN

## Para desarrollo

1. sh scripts/pre-commit.sh
1. docker-compose build
1. docker-compose up django
1. (en otra terminal) docker-compose exec django bash
1. python manage.py migrate
1. python manage.py createsuperuser
1. docker-compose stop
1. docker-compose up django beat worker flower (recuerda reiniciar beat y worker cuando estes creando nuevas tasks de celery, ellos no se reinician automaticamente)

## Para producción

1. export COMPOSE_FILE=prod/docker-compose.yml
1. docker-compose build
1. docker tag codebase_django:latest < nombre del registry en donde quieres subir >
1. docker push < nombre del registry en donde quieres subir >
