# Django and DRF imports
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# waning_moon_design imports
from new_activity_sept2023.permissions import (
    IsUserDniAndIsAuthenticatedCar,
    IsUserIsStaffAndIsAuthenticatedWorker,
    IsUserDniAndIsStaffAndIsAuthenticatedWorkshop,
    IsUserDniAndPhoneNumberAndIsAuthenticatedRepair
)
from new_activity_sept2023.models import Workshop, Car, Repair, Worker
from new_activity_sept2023.serializers import (
    WorkshopSerializer,
    WorkerSerializer,
    CarSerializer,
    RepairWorkerCarSerializer,
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

    def get_permissions(self):
        if self.action == 'create':
            permissions_classes = [IsUserDniAndIsStaffAndIsAuthenticatedWorkshop]
        else:
            permissions_classes = self.permission_classes
        return [permission() for permission in permissions_classes]


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

    def get_permissions(self):
        if self.action == 'create':
            permissions_classes = [IsUserIsStaffAndIsAuthenticatedWorker]
        else:
            permissions_classes = self.permission_classes
        return [permission() for permission in permissions_classes]


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

    def get_permissions(self):
        if self.action == 'create':
            permissions_classes = [IsUserDniAndIsAuthenticatedCar]
        else:
            permissions_classes = self.permission_classes
        return [permission() for permission in permissions_classes]


class RepairViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet
                    ):
    queryset = Repair.objects.all()
    serializer_class = RepairWorkerCarSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "date_time": ["exact"],
    }
    search_fields = ['car__car_license_plate']
    ordering_fields = ['date_time']

    def get_permissions(self):
        if self.action == 'create':
            permissions_classes = [IsUserDniAndPhoneNumberAndIsAuthenticatedRepair]
        else:
            permissions_classes = self.permission_classes
        return [permission() for permission in permissions_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return RepairSerializer
        return RepairWorkerCarSerializer
