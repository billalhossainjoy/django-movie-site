from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from movies.models import Movie, Genre
from movies.permissions import IsOwnerOrReadOnly
from movies.serializer import MovieSerializer, GenreSerializer



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ListCreateMovie(ListCreateAPIView):
    queryset = (
        Movie.objects
        .select_related("created_by")
        .prefetch_related("genres")
    )
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "release_year",
        "genres",
    ]

    search_fields = [
        "title",
        "description",
        "director",
        "genres__name",
    ]

    ordering_fields = [
        "title",
        "release_year",
        "created_at",
        "updated_at",
    ]

    ordering = [
        "-created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(
            created_by= self.request.user,
        )

class GetUpdateDeleteMovie(RetrieveUpdateDestroyAPIView):
    queryset = (
        Movie.objects
        .select_related("created_by")
        .prefetch_related("genres")
    )
    serializer_class = MovieSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

class ListCreateGenre(ListCreateAPIView):
    queryset = Genre.objects.all().order_by("name")
    serializer_class = GenreSerializer
    pagination_class = CustomPagination

    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class GetUpdateDeleteGenre(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]