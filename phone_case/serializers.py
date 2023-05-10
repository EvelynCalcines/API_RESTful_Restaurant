# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from .models import PhoneCase


class PhoneCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneCase
        fields = "__all__"
