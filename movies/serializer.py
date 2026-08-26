from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['id']

class MovieSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Movie
        fields = '__all__'

        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at",
        ]