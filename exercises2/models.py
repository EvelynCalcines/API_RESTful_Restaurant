# Python imports
import uuid

# Django and DRF imports
from django.db import models

# waning_moon_design imports
from utils.models import BaseModel
from authentication.models import User


class ColorType(models.TextChoices):
    RED = "R", "Rojo"
    BLUE = "Az", "Azul"
    WHITE = "B", "Blanco"
    GRAY = "G", "Gris"

    @classmethod
    def get_all_choices(cls):
        return {choice.value: choice.label for choice in cls}


class Building(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number_floors = models.IntegerField()
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    color = models.CharField(max_length=100, choices=ColorType.choices)
    total_floors = models.IntegerField()

    class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.street}"


class Floor(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    square_meters = models.FloatField()
    number_rooms = models.PositiveIntegerField()
    number_bathrooms = models.PositiveIntegerField()
    floor = models.IntegerField()
    letter = models.CharField(max_length=1)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Floor"
        verbose_name_plural = "Floors"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.floor} {self.letter}"
