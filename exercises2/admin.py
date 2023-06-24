# Django and DRF imports
from django.contrib import admin

# waning_moon_design imports
from .models import Building, Floor


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('number_floors', 'street', 'number', 'color', 'total_floors', 'created_at', 'updated_at',
                    'deleted_at', 'active')

    list_filter = ('color', 'number')
    search_fields = ('street', 'number_floors', 'total_floors')


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('square_meters', 'floor', 'letter', 'building', 'user', 'created_at', 'updated_at',
                    'deleted_at', 'active')

    list_filter = ('floor', 'letter')
    search_fields = ('number_rooms', 'number_bathrooms')
