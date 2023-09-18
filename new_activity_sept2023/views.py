# Django and DRF imports
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


class WorkerViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet
                    ):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = 'id'


class CarViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 GenericViewSet
                 ):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'


class RepairViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet
                    ):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    lookup_field = 'id'
