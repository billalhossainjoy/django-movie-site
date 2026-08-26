from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        request = self.context.get("request")

        user = authenticate(request, username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        attrs['user'] = user
        return attrs

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
    )

    password_confirm = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "password",
            "password_confirm",
        ]

        read_only_fields = [
            "id",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({
                "password_confirm": "Passwords do not match."
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")

        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user