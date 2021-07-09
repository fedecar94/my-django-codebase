from .settings import *  # noqa

print("DEBUG!")

DEBUG = True

MIDDLEWARE = [MIDDLEWARE[0], "whitenoise.middleware.WhiteNoiseMiddleware"] + MIDDLEWARE[1:]  # noqa

ALLOWED_HOSTS = ["*"]
