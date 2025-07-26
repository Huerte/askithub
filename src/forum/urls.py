from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('room/<str:room_id>', views.enter_room, name='enter_room'),
]