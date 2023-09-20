# Django and DRF imports
from rest_framework import serializers

# waning_moon_design imports
from new_activity_sept2023.models import Workshop
from new_activity_sept2023.models import Worker
from new_activity_sept2023.models import Car
from new_activity_sept2023.models import Repair


class WorkshopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workshop
        fields = "__all__"


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"


class RepairSerializer(serializers.ModelSerializer):

    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    workers = serializers.PrimaryKeyRelatedField(many=True, queryset=Worker.objects.all())

    class Meta:
        model = Repair
        fields = "__all__"


class RepairWorkerCarSerializer(serializers.ModelSerializer):

    car = CarSerializer()
    workers = WorkerSerializer(many=True)

    class Meta:
        model = Repair
        fields = "__all__"


