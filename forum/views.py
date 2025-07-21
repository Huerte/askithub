from django.shortcuts import render


def homepage_view(requests):
    return render(requests, 'forum/home.html')

def login_view(requests):
    return render(requests, 'forum/auth/login.html')

def register_view(requests):
    return render(requests, 'forum/auth/register.html')