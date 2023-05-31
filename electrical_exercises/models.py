# Django and DRF imports
from django.db import models

# Python imports
import uuid

# waning_moon_design imports
from utils.models import BaseModel


class Television(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inches = models.IntegerField()
    serial_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'Television: {self.serial_number}'


class Fridge(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'Color Fridge: {self.color}'
