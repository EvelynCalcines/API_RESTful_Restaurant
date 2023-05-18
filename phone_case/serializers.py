# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from .models import PhoneCase


class PhoneCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCase
        fields = "__all__"


class UpdatePhoneCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCase
        fields = "__all__"
        read_only_fields = ["id", "stock", "brand", "model"]

