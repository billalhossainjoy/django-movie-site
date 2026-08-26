from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Review
        fields = "__all__"

        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        request = self.context["request"]

        movie = attrs.get("movie")

        queryset = Review.objects.filter(
            user=request.user,
            movie=movie,
        )

        if self.instance:
            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():
            raise serializers.ValidationError({
                "movie": "You have already reviewed this movie."
            })

        return attrs