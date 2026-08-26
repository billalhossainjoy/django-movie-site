from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.models import Review
from reviews.permissions import IsReviewOwnerOrReadOnly
from reviews.serializers import ReviewSerializer

class ListViewReview(ListCreateAPIView):
    queryset = Review.objects.select_related("user", "movie").all()
    serializer_class =  ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

class GetUpdateDeleteReview(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.select_related("user", "movie")

    serializer_class = ReviewSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsReviewOwnerOrReadOnly
    ]