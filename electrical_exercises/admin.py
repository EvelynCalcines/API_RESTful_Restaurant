# Django and DRF imports
from django.contrib import admin

# waning_moon_design imports
from .models import Fridge, Television


@admin.register(Television)
class TelevisionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('inches', 'serial_number', 'created_at', 'updated_at', 'deleted_at', 'active')


@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('width', 'height', 'color', 'created_at', 'updated_at', 'deleted_at', 'active')
