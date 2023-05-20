# Django and DRF imports
from django.contrib import admin

# waning_moon_design imports
from .models import PhoneCase


@admin.register(PhoneCase)
class PhoneCaseAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('name', 'color', 'phrase', 'design', 'created_at', 'updated_at', 'deleted_at', 'active')
    list_filter = ('color', 'stock')
    search_fields = ('name', 'brand', 'model')
