from django.urls import path

from movies.api_views import ListCreateMovie, GetUpdateDeleteMovie

urlpatterns= [
    # movies
    path('', ListCreateMovie.as_view(), name='list-create-movie'),
    path('<int:id>', GetUpdateDeleteMovie.as_view(), name='get-update-delete-movie'),

    # genres
    path('', ListCreateMovie.as_view(), name='list-create-genre'),
    path('<int:id>', GetUpdateDeleteMovie.as_view(), name='get-update-delete-genre')
]

