# Python imports
import uuid

# Django and DRF imports
from django.db import models

# waning_moon_design imports
from utils.models import BaseModel


class Restaurant(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=9)

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return f"Restaurant: {self.name}"
