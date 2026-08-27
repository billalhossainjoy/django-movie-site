from django.urls import path

from accounts.api_views import login_api, signup_api, user_api, csrf_api, logout_api

urlpatterns = [
    path("csrf", csrf_api, name="api-csrf"),
    path("login/", login_api, name="login-api"),
    path("signup/", signup_api, name="signup-api"),
    path("user/", user_api, name="user-api"),
    path("logout/", logout_api, name="api-logout"),
]