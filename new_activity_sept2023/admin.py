# Django and DRF imports
from django.contrib import admin

# waning_moon_design imports
from .models import Workshop, Worker, Car, Repair


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('name', 'address', 'cif', 'id',
                    'created_at', 'updated_at', 'deleted_at', 'active')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('name', 'dni', 'number_phone', 'id', 'workshop',
                    'created_at', 'updated_at', 'deleted_at', 'active')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('car_license_plate', 'brand', 'model', 'color', 'id',
                    'created_at', 'updated_at', 'deleted_at', 'active')


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('worker', 'car', 'date_time', 'id',
                    'created_at', 'updated_at', 'deleted_at', 'active')
