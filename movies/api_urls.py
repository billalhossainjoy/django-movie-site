from django.urls import path

from movies.api_views import ListCreateMovie, GetUpdateDeleteMovie, ListCreateGenre, GetUpdateDeleteGenre

urlpatterns= [
    # movies
    path('', ListCreateMovie.as_view(), name='list-create-movie'),
    path('<uuid:pk>/', GetUpdateDeleteMovie.as_view(), name='get-update-delete-movie'),

    # genres
    path('genres/', ListCreateGenre.as_view(), name='list-create-genre'),
    path('genres/<uuid:pk>/', GetUpdateDeleteGenre.as_view(), name='get-update-delete-genre')
]

