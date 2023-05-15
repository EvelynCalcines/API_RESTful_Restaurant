# Django and DRF imports
from django.contrib import admin

# waning_moon_design imports
from .models import PhoneCase


@admin.register(PhoneCase)
class PhoneCaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'phrase', 'design', 'created_at', 'updated_at')
    list_filter = ('color', 'stock')
    search_fields = ('name', 'brand', 'model')
