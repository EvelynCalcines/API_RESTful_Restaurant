# Django and DRF imports
import django_filters
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

# waning_moon_design imports
from restaurant_technical_test.models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "address": ["icontains", "exact", "istartswith"],
        "phone": ["lt", "exact", "gt"],
    }
    search_fields = ['name']
    ordering_fields = ['address']

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            # Validación: Asegurarse de que el teléfono tenga un formato válido
            if not data.get('phone').isdigit() or len(data.get('phone')) != 10:
                raise serializers.ValidationError("El número de teléfono no es válido")
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as _:
            return Response({"error": "Error al crear el restaurante"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as _:
            return Response({"error": "Error al actualizar el restaurante"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as _:
            return Response({"error": "Error al eliminar el restaurante"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
