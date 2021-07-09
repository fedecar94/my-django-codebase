from django.test import TestCase

from apps.testing.models import TestingModel


class TestingModelTests(TestCase):
    def test_creation_model(self):
        instance = TestingModel.objects.create(value=1)
        self.assertEquals(instance.value, 1)
