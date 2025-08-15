from django.urls import path
from . import views


urlpatterns = [
    path('answer/<str:room_id>', views.comment, name='answer_question'),
    path('remove-answer/<str:comment_id>', views.remove_comment, name='remove_answer'),
    path('edit-answer/<str:answer_id>', views.edit_answer, name='edit_answer'),
    path('answer/<int:answer_id>/get/', views.get_answer_body, name='get_answer_body'),

    path('add-question/', views.add_question, name='add_question'),
    path('delete-question/<str:room_id>', views.delete_question, name='delete_question'),
]