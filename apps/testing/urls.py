from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import TestingModelViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"testing", TestingModelViewSet)
