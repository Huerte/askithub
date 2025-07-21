from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('login/', views.login_view, name='login-page')
]