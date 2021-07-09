from uuid import uuid4
from django.db import models
from datetime import datetime


def gen_uuid() -> str:
    timestamp = hex(int(datetime.utcnow().timestamp() * 1000000))[2:]
    uid = str(uuid4())
    return f"{timestamp[:8]}-{timestamp[8:-1]}-{uid[14:]}"


class TimestampedModel(models.Model):
    id = models.UUIDField(default=gen_uuid, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
