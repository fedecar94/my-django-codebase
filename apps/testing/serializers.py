from rest_framework import serializers

from apps.testing.models import TestingModel


class TestingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingModel
        fields = ["id", "created", "value"]
