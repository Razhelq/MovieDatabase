from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class Movie(admin.ModelAdmin):
    list_display = ['title', 'year', 'type', 'imdb_id', 'poster']
