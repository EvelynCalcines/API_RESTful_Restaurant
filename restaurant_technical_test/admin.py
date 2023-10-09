# Django and DRF imports
from django.contrib import admin

# waning_moon_design imports
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('name', 'address', 'phone', 'created_at', 'updated_at',
                    'deleted_at', 'active')
    list_filter = ('name', 'address')
    search_fields = ('name', 'brand', 'phone')
