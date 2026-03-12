from django.contrib import admin
from .models import Tour, Category, Tourist, Review

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('categories',) # Удобный виджет для ManyToMany

admin.site.register(Category)
admin.site.register(Tourist)
admin.site.register(Review)