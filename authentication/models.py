# Python imports
import uuid

# Django and DRF imports
from django.db import models
from django.contrib.auth.models import Permission, Group, AbstractBaseUser, PermissionsMixin

# waning_moon_design imports
from utils.models import BaseModel


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True,  blank=True)
    address = models.CharField(max_length=200, null=True,  blank=True)
    is_staff = models.BooleanField(default=False)

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        verbose_name='user permissions',
        related_name='user_set_custom',
        related_query_name='user_custom'
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        verbose_name='groups',
        related_name='user_set_custom',
        related_query_name='user_custom'
    )

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
