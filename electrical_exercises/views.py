# Django and DRF imports
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


class FridgeViewSet(CreateModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Fridge.objects.all()
    serializer_class = FridgeSerializer
    lookup_field = 'id'
