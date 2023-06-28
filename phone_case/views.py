# Django and DRF imports
import django_filters
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# waning_moon_design imports
from phone_case.models import PhoneCase
from .serializers import (UpdatePhoneCaseSerializer,
                          ListPhoneCaseSerializer,
                          CreatePhoneCaseSerializer,
                          ListProfilePhoneCaseSerializer)


class PhoneCaseViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
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

    def get_permissions(self):
        if self.action in ['create', 'favorite', 'unfavorite']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
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
            return CreatePhoneCaseSerializer
        return self.serializer_class

    @action(detail=True, methods=['POST'])
    def favorite(self, request, id):
        phonecase = self.get_object()
        self.request.user.favorite(phonecase)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def unfavorite(self, request, id):
        phonecase = self.get_object()
        self.request.user.unfavorite(phonecase)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MePhoneCaseView(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):

    queryset = PhoneCase.objects.all()
    serializer_class = ListProfilePhoneCaseSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user.id)
        return queryset

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return UpdatePhoneCaseSerializer
        return self.serializer_class
