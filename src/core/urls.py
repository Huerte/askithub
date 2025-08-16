from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('all-room/', views.all_question_view, name='all_room'),
    path('about/', views.about_view, name='about_page'),
    path('related-questions/<str:topic_id>', views.visit_topics, name='visit_related_topics'),
    path('explore/topics/', views.explore_topics, name='explore_topics'),
    path('room/<str:room_id>', views.enter_room, name='enter_room'),

    path('search/', views.search_page, name='search'),
]