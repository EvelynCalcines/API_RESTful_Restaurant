# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from .models import ColorType, Building, Floor
from authentication.serializers import UserProfileSerializer


class ListBuildingSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Building
        fields = "__all__"


class CreateBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class UpdateBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = "__all__"
        read_only_fields = ["id", "street", "number", "total_floors", "number_floors"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


#  A partir de aquí empieza floor.

class ListProfileFloorSerializer(serializers.ModelSerializer):
    building = ListBuildingSerializer()
    user = UserProfileSerializer()

    class Meta:
        model = Floor
        fields = "__all__"


class ListFloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        exclude = ["created_at", "updated_at", "deleted_at", "active"]


class CreateFloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = "__all__"


class UpdateFloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = "__all__"
        read_only_fields = ["id", "floor", "letter", "square_meters"]
