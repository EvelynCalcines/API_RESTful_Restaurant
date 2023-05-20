# Python imports
from datetime import datetime

# Django and DRF imports
from django.db import models


class ActiveItemManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    active = models.BooleanField(default=True)

    objects = ActiveItemManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        if self.active:
            self.active = False
            self.deleted_at = datetime.now()
            return self.save(update_fields=["active", "deleted_at"])