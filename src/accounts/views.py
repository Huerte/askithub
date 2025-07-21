from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login


def login_view(request):
    return render(request, 'auth/login.html')

def register_view(request):
    return render(request, 'auth/register.html')


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            redirect('homepage')

    return redirect('login-page')


def register_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            print('Username already existed')
        elif User.objects.filter(email=email).exists():
            print('Email already existed')
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()

            return redirect('login-page')

    return redirect('register-page')
