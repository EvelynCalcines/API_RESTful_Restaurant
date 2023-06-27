# Django and DRF imports
import django_filters
from rest_framework import mixins, permissions, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

# waning_moon_design imports
from exercises2.models import Building, Floor
from exercises2.serializers import (
    ListBuildingSerializer,
    ListFloorSerializer,
    CreateFloorSerializer,
    ListProfileFloorSerializer,
    UpdateFloorSerializer,
    UpdateBuildingSerializer
)


class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ListBuildingSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "number_floors": ["lt", "lte", "exact", "gte", "gt"],
        "number": ["lt", "lte", "exact", "gte", "gt", "in"],
        "total_floors": ["lt", "lte", "exact", "gte", "gt"]
    }
    search_fields = ['street']
    ordering_fields = "__all__"

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return UpdateBuildingSerializer
        return self.serializer_class


class FloorViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Floor.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ListFloorSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "number_rooms": ["lt", "lte", "exact", "gte", "gt"],
        "square_meters": ["lt", "lte", "exact", "gte", "gt", "in"],
        "number_bathrooms": ["lt", "lte", "exact", "gte", "gt", "in"],
        "letter": ["icontains", "exact"],
        "floor": ["lt", "lte", "exact", "gte", "gt"],
        "user": ["exact", "isnull"],
        "building": ["exact", "in"]

    }
    search_fields = ['name', 'user__first_name']
    ordering_fields = ['building__street']

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateFloorSerializer
        return self.serializer_class


class MeFloorView(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Floor.objects.all()
    serializer_class = ListProfileFloorSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user.id)
        return queryset

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return UpdateFloorSerializer
        return self.serializer_class
