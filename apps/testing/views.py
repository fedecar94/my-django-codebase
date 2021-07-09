from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import TestingModel
from .serializers import TestingModelSerializer
from .filters import TestingModelFilter


class TestingModelViewSet(GenericViewSet, ListModelMixin):
    serializer_class = TestingModelSerializer
    queryset = TestingModel.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    filterset_class = TestingModelFilter
    search_fields = ['value']
    ordering_fields = ['value', 'created']
    pagination_class = LimitOffsetPagination

    @action(methods=["get"], detail=False)
    def first(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer_class()
        return Response(serializer(queryset.first()).data, status=HTTP_200_OK)
