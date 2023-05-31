# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from electrical_exercises.models import Television
from electrical_exercises.models import Fridge


class TelevisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Television
        fields = "__all__"

    def create(self, data):
        television = Television.objects.create(**data)
        return television

    def update(self, instance, data):  # PUT
        instance.inches = data.get("inches", instance.inches)
        instance.serial_number = data.get("serial_number", instance.serial_number)
        instance.save()
        return instance


class FridgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fridge
        fields = "__all__"

    def create(self, data):
        fridge = Fridge.objects.create(width=5, height=2, color="negro")
        return fridge

    def update(self, instance, data):  # PATCH
        instance.height = data.get('height', instance.height)
        instance.width = data.get('width', instance.width)
        instance.color = data.get('color', instance.color)

        instance.save(update_fields=['height', 'width'])

        return instance
