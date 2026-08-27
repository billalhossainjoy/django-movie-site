from django.middleware.csrf import get_token
from django.template.context_processors import csrf
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import login, logout
from accounts.serializers import LoginSerializer, SignUpSerializer

@api_view(["GET"])
@permission_classes([AllowAny])
def csrf_api(request):
    return Response({
        "csrf_token": get_token(request)
    })


@api_view(["POST"])
@permission_classes([AllowAny])
def login_api(request):
    serializer = LoginSerializer(data=request.data, context={'request': request})

    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']

    login(request, user)

    return Response({
        'message': "Login successful",
        'user': {
            "id": user.id,
            "username": user.username,
        },
    })

@api_view(["POST"])
@permission_classes([AllowAny])
def signup_api(request):
    serializer = SignUpSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    return Response(
        {
            "message": "User created successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        },
        status=status.HTTP_201_CREATED,
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_api(request):
    return Response({
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_api(request):
    logout(request)

    return Response({
        "message": "Logout successful"
    })