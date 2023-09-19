# Python imports
import uuid

# Django and DRF imports
from django.db import models

# waning_moon_design imports
from utils.models import BaseModel


class Workshop(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    cif = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Workshop"
        verbose_name_plural = "Workshops"

    def __str__(self):
        return f"Workshop: {self.name}"


class Worker(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    number_phone = models.IntegerField(null=True, blank=True)
    dni = models.CharField(max_length=20, unique=True)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='workers')

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return f"Workers: {self.name}"


class Car(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car_license_plate = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"Car: {self.brand} {self.model}"


class Repair(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_time = models.DateTimeField()
    workers = models.ManyToManyField('Worker', related_name='repairs')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Repair"
        verbose_name_plural = "Repairs"

    def __str__(self):
        return f"Repair on {self.date_time} for {self.car}"
