# Python imports
import uuid

# Django and DRF imports
from django.db import models

# waning_moon_design imports
from utils.models import TimestampedModel


class PhoneCase(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.IntegerField()
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    phrase = models.CharField(max_length=255)
    design = models.TextField()

    class Meta:
        verbose_name = "PhoneCase"
        verbose_name_plural = "PhoneCases"

    def __str__(self):
        return f"{self.name}"
