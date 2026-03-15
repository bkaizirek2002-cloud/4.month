from django.contrib import admin
from .models import DriverModel

@admin.register(DriverModel)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'experience', 'has_license')