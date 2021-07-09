from django.contrib import admin
from apps.testing.models import TestingModel


@admin.register(TestingModel)
class TestModelAdmin(admin.ModelAdmin):
    pass
