from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login-page'),
    path('register/', views.register_view, name='register-page'),

    path('login/account/', views.login_user, name='login'),
    path('register/account/', views.register_user, name='register'),
]