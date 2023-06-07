# Django and DRF imports
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

# waning_moon_design imports
from electrical_exercises.models import Television, Fridge
from electrical_exercises.serializers import TelevisionSerializer, FridgeSerializer


class TelevisionViewSet(ModelViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'serial_number'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "inches": ["icontains", "isnull", "exact", "in"],
        "serial_number": ["lt", "lte", "exact", "gte", "gt", "in"],
    }
    search_fields = ['inches', "serial_number"]
    ordering_fields = "__all__"


class FridgeViewSet(CreateModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Fridge.objects.all()
    serializer_class = FridgeSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "color": ["icontains", "isnull", "exact", "in"],
        "height": ["lt", "lte", "exact", "gte", "gt", "in"],
    }
    search_fields = ['color']
    ordering_fields = ['color']
