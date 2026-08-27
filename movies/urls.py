from django.urls import path

from movies.views import movie_list, movie_detail_page

urlpatterns = [
    path("", movie_list, name="movie-list-page"),

    path(
        "<uuid:pk>/",
        movie_detail_page,
        name="movie-detail-page",
    ),
]