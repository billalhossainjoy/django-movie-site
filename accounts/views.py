from django.shortcuts import render


def login_page(request):
    return render(request, "accounts/login.html")

def signup_page(request):
    return render(request, "accounts/signup.html")

