from django.db import models
from apps.base.models import TimestampedModel


class TestingModel(TimestampedModel):
    value = models.IntegerField(default=0)
