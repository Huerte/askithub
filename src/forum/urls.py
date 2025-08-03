from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('all-room/', views.all_question_view, name='all_room'),
    path('about/', views.about_view, name='about_page'),

    path('profile-page/', views.profile_view, name='profile_page'),

    path('room/<str:room_id>', views.enter_room, name='enter_room'),
    path('answer/<str:room_id>', views.comment, name='answer_question'),
    path('remove-answer/<str:comment_id>', views.remove_comment, name='remove_answer'),
    path('edit-answer/<str:answer_id>', views.edit_answer, name='edit_answer'),
    path('answer/<int:answer_id>/get/', views.get_answer_body, name='get_answer_body'),

    path('add-question/', views.add_question, name='add_question'),
    path('delete-question/<str:room_id>', views.delete_question, name='delete_question'),

    path('related-questions/<str:topic_id>', views.visit_topics, name='visit_related_topics'),
    path('search/', views.search_page, name='search'),
]