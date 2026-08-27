from django.urls import path

from reviews.api_views import ListViewReview, GetUpdateDeleteReview

urlpatterns = [
    path('', ListViewReview.as_view(), name="list-create-review"),
    path('<uuid:pk>', GetUpdateDeleteReview.as_view(), name="get-update-delete-review"),
]
