from django.contrib import admin
from .models import Car 

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'price', 'engine_volume', 'color', 'is_electric', 'brand')
    search_fields = ('title', 'brand')
    list_filter = ('year', 'is_electric', 'brand')