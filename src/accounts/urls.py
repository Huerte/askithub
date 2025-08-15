from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login-page'),
    path('register/', views.register_view, name='register-page'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),

    path('login/account/', views.login_user, name='login'),
    path('register/account/', views.register_user, name='register'),
    path('logout/account/', views.logout_user, name='logout'),

    path('profile-update/', views.update_profile, name='update_profile'),

    path('visit-profile/<str:user_id>', views.visit_profile, name='visit_profile'),

    path('follow-profile/<str:user_id>', views.follow_user, name='follow_user'),
    path('unfollow-profile/<str:user_id>', views.unfollow_user, name='unfollow_user'),

    path('followers/<str:user_id>', views.view_followers, name='visit_followers'),
    path('following/<str:user_id>', views.view_following, name='visit_following'),

    path('user/activity/<str:user_id>', views.view_user_activities, name='view_user_activities'),

]