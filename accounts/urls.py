from django.urls import path

from accounts.api_views import login_api
from accounts.views import login_page, signup_page

urlpatterns = [
    path('signup/', signup_page, name='signup-page'),
    path('login/', login_page, name='login-page'),
]