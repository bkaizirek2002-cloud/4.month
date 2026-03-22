from django.contrib import admin
from .models import Movie, Genre, Tag, Comment

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_date', 'rating']
    list_filter = ['genre', 'tags']
    search_fields = ['title']

admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Comment)