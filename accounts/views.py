from django.shortcuts import render


def login_view(requests):
    return render(requests, 'accounts/auth/login.html')

def register_view(requests):
    return render(requests, 'accounts/auth/register.html')