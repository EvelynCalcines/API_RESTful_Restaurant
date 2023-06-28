# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from .models import PhoneCase, ColorType
from authentication.serializers import UserProfileSerializer


class ListPhoneCaseSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')
    user = UserProfileSerializer()
    is_favorite = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = PhoneCase
        exclude = ["created_at", "updated_at", "deleted_at", "active"]

    def get_is_favorite(self, obj):
        return self.context["request"].user.is_favorite(obj)

    def get_favorites(self, obj):
        return obj.favorites()


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
