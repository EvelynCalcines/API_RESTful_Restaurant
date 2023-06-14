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
    YELLOW = "Am", "Amarillo"
    BLACK = "N", "Negro"
    BROWN = "M", "Marron"
    WHITE = "B", "Blanco"
    PINK = "Rs", "Rosa"
    GREEN = "V", "Verde"
    GRAY = "G", "Gris"
    ORANGE = "Na", "Naranja"
    PURPLE = "Mo", "Morado"
    SILVER = "P", "Plateado"
    GOLDEN = "D", "Dorado"
    TRANSPARENT = "T", "Transparente"

    @classmethod
    def get_all_choices(cls):
        return {choice.value: choice.label for choice in cls}


class PhoneCase(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.IntegerField()
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=50, choices=ColorType.choices)
    phrase = models.CharField(max_length=255)
    design = models.TextField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "PhoneCase"
        verbose_name_plural = "PhoneCases"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"
