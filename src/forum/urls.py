from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('room/<str:room_id>', views.enter_room, name='enter_room'),
    path('answer/<str:room_id>', views.comment, name='answer_question'),
    path('remove-answer/<str:comment_id>', views.remove_comment, name='remove_answer'),
    path('add_question/', views.add_question, name='add_question'),
]