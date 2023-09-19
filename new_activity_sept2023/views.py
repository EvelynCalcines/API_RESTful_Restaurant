# Django and DRF imports
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# waning_moon_design imports
from new_activity_sept2023.models import Workshop, Car, Repair, Worker
from new_activity_sept2023.serializers import (
    WorkshopSerializer,
    WorkerSerializer,
    CarSerializer,
    RepairSerializer
)


class WorkshopViewSet(ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains", "exact", "istartswith"],
        "cif": ["istartswith", "exact", "icontains"],
    }
    search_fields = ['name']
    ordering_fields = ['address']


class WorkerViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet
                    ):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains", "exact", "istartswith"],
        "dni": ["istartswith", "exact", "icontains"],
    }
    search_fields = ['name']
    ordering_fields = ['dni']


class CarViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 GenericViewSet
                 ):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "car_license_plate": ["lt", "exact", "gt"],
        "brand": ["exact", "istartswith"],
        "model": ["exact", "istartswith"],

    }
    search_fields = ['brand']
    ordering_fields = ['model']


class RepairViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet
                    ):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "date_time": ["exact"],
    }
    search_fields = ['car__car_license_plate']
    ordering_fields = ['date_time']
