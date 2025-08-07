from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from .models import UserStatus, Profile
from django.utils import timezone
from forum.models import QuestionThread


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

            update_user_status(request)
            
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

@login_required(login_url='/auth/login/')
def logout_user(request):
    update_user_status(request)

    UserStatus.objects.update_or_create(
        user=request.user,
        defaults={'is_online': False}
    )
    
    logout(request)
    return redirect('login-page')

@login_required(login_url='/auth/login')
def update_profile(request):
    update_user_status(request)


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
    update_user_status(request)

    user = User.objects.get(id=user_id)
    profile, _ = Profile.objects.get_or_create(user=user)
    user_status, _ = UserStatus.objects.get_or_create(user=user)
    try:
        users_questions = QuestionThread.objects.filter(created_by=user)
    except QuestionThread.DoesNotExist:
        users_questions = None

    is_followed = False
    if request.user != user:
        is_followed = profile.followers.filter(user=request.user).exists()

    context = {
        'profile': profile,
        'user_status': user_status,
        'users_questions': sorted(users_questions, key=lambda users_questions: users_questions.created_at),
        'questions_count': len(users_questions),
        'following': profile.following.all(),
        'following_count': profile.following.count(),
        'followers': profile.followers.all(),
        'followers_count': profile.followers.count(),
        'is_followed': is_followed,
    }

    return render(request, 'section/profile-page.html', context)

@login_required(login_url='/auth/login/')
def update_user_status(request):
    user_status, _ = UserStatus.objects.get_or_create(user=request.user)
    user_status.last_seen = timezone.now()
    user_status.save()


@login_required(login_url='/auth/login/')
def follow_user(request, user_id):

    user = User.objects.get(id=user_id)
    my_profile, _ = Profile.objects.get_or_create(user=request.user)
    target_profile, _ = Profile.objects.get_or_create(user=user)

    my_profile.following.add(target_profile)

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/auth/login/')
def unfollow_user(request, user_id):

    user = User.objects.get(id=user_id)
    my_profile, _ = Profile.objects.get_or_create(user=request.user)
    target_profile, _ = Profile.objects.get_or_create(user=user)

    my_profile.following.remove(target_profile)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='/auth/login/')
def view_followers(request, user_id):

    user = User.objects.get(id=user_id)
    target_profile, _ = Profile.objects.get_or_create(user=user)

    context = {
        'followers': target_profile.followers.all(),
    }

    return render(request, 'section/followers-section.html', context)

@login_required(login_url='/auth/login/')
def view_following(request, user_id):

    user = User.objects.get(id=user_id)
    target_profile, _ = Profile.objects.get_or_create(user=user)

    context = {
        'following': target_profile.following.all(),
    }

    return render(request, 'section/following-section.html', context)