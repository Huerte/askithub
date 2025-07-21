from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('login/', views.login_view, name='login-page'),
    path('register/', views.register_view, name='register-page'),
]