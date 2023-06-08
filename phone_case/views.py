# Django and DRF imports
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

# waning_moon_design imports
from .serializers import UpdatePhoneCaseSerializer, ListPhoneCaseSerializer, CreatePhoneCaseSerializer
from phone_case.models import PhoneCase


class PhoneCaseViewSet(ModelViewSet):
    queryset = PhoneCase.objects.all()
    serializer_class = ListPhoneCaseSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "color": ["icontains", "isnull", "exact", "in"],
        "stock": ["lt", "lte", "exact", "gte", "gt", "in"],
    }
    search_fields = ['name']
    ordering_fields = ['brand']

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdatePhoneCaseSerializer
        elif self.action == "create":
            return CreatePhoneCaseSerializer
        return self.serializer_class
