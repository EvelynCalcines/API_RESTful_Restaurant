# Django and DRF imports
from django.contrib import admin

# waning_moon_design imports
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('id', 'first_name', 'last_name', 'email', 'deleted_at', 'active', 'is_superuser')
    list_filter = ('active',)
    search_fields = ('first_name', 'last_name', 'email')
