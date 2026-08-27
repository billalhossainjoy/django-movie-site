from django.shortcuts import render
from .models import Movie


def movie_list(request):
    return render(
        request,
        "movies/movie_list.html",
    )

def movie_detail_page(request, pk):
    return render(
        request,
        "movies/detail.html",
        {
            "movie_id": pk,
        },
    )