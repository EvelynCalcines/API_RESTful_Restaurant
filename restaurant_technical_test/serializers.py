# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from .models import Restaurant


def validate_name(self, value):
    # Validación: El nombre del restaurante no debe contener números
    if any(char.isdigit() for char in value):
        raise serializers.ValidationError("El nombre no debe contener números")
    return value


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


