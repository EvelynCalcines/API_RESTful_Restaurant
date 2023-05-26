# Python imports
from datetime import datetime

# Django and DRF imports
from django.db import models


class ActiveItemManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(active=True)

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


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
