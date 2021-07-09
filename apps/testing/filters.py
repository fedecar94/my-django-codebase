from django_filters import rest_framework as filters

from apps.testing.models import TestingModel


class TestingModelFilter(filters.FilterSet):
    class Meta:
        model = TestingModel
        fields = {
            "created": ["exact", "in", "gt", "gte", "lt", "lte"],
            "value": ["exact", "in", "gt", "gte", "lt", "lte"],
        }
