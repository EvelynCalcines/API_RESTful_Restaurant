# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from .models import ColorType, Building, Floor


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

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Building
        fields = "__all__"
        read_only_fields = ["id", "street", "number", "total_floors", "number_floors"]


#  A partir de aquí empieza floor.


class ListFloorSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Building
        fields = "__all__"


class CreateFloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class UpdateFloorSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Floor
        fields = "__all__"
        read_only_fields = ["id", "floor", "letter", "square_meters"]
