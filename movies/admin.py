from django.contrib import admin

from movies.models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

    search_fields = ["name"]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "release_year",
        "director",
        "created_by",
        "created_at",
    ]
    list_filter = [
        "release_year",
        "genres",
    ]

    search_fields = [
        "title",
        "director",
    ]

    filter_horizontal = [
        "genres",
    ]