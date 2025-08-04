from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
import logging
from .models import UserStatus, Profile


# Get a logger instance
logger = logging.getLogger(__name__)


def login_view(request):
    return render(request, 'auth/login.html')

def register_view(request):
    return render(request, 'auth/register.html')

def forgot_password_view(request):
    return render(request, 'auth/forgot-password.html')

@requires_csrf_token
def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user=user)
            UserStatus.objects.update_or_create(
                user=user,
                defaults={'is_online': True}
            )

            return redirect('homepage')

    return redirect('login-page')

@requires_csrf_token
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

def logout_user(request):
    UserStatus.objects.update_or_create(
        user=request.user,
        defaults={'is_online': False}
    )
    
    logout(request)
    return redirect('login-page')

@login_required(login_url='/auth/login')
def profile_view(request):

    profile, _ = Profile.objects.get_or_create(user=request.user)

    context = {
        'profile': profile,
        'avatar': profile.avatar
    }
    
    return render(request, 'section/profile-page.html', context)

@login_required(login_url='/auth/login')
def update_profile(request):

    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)

        if request.FILES.get('avatar'):
            profile.avatar = request.FILES['avatar']

        bio = request.POST.get('bio')
        if bio:
            profile.bio = bio

        profile.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/auth/login/')
def visit_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile, _ = Profile.objects.get_or_create(user=user)

    context = {
        'profile': profile,
    }

    return render(request, 'section/profile-page.html', context)