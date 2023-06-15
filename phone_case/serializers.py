# Django and DRF imports
from rest_framework import serializers


# waning_moon_design imports
from .models import PhoneCase, ColorType


class ListPhoneCaseSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = PhoneCase
        exclude = ["created_at", "updated_at", "deleted_at", "active"]


class ListProfilePhoneCaseSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = PhoneCase
        fields = "__all__"


class CreatePhoneCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneCase
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class UpdatePhoneCaseSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = PhoneCase
        fields = "__all__"
        read_only_fields = ["id", "stock", "brand", "model", "color"]
