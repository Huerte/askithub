from django.shortcuts import render


def login_view(requests):
    return render(requests, 'auth/login.html')

def register_view(requests):
    return render(requests, 'auth/register.html')