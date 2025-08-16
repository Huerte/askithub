from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q
from forum.models import QuestionThread, Answer, Topic
from django.db import models
from django.contrib.auth.decorators import login_required
from accounts.views import update_user_status


def homepage_view(request):

    question_thread = QuestionThread.objects.all()[::-1][:5]
    topics = Topic.objects.all()[:5]

    context = {
        'question_thread': question_thread,
        'topics': topics,
    }

    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'section/about-page.html')

def all_question_view(request):
    question_thread = QuestionThread.objects.select_related('created_by', 'topic').prefetch_related('answers').all().order_by('-created_at')

    context = {
        'all_questions': question_thread,
    }

    return render(request, 'section/explore-page.html', context)

@login_required(login_url='/auth/login')
def enter_room(request, room_id):
    update_user_status(request)

    question_thread = QuestionThread.objects.get(id=room_id)
    answers = question_thread.answers.all()

    if request.user.is_authenticated:
        question_thread.mark_seen(request.user)

    context = {
        'question_thread': question_thread,
        'answers': answers,
    }

    return render(request, 'section/room.html', context)

def visit_topics(request, topic_id):

    topic = get_object_or_404(Topic, id=topic_id)
    questions = QuestionThread.objects.filter(topic=topic)

    context = {
        'questions': questions,
        'topic': topic,
    }

    return render(request, 'section/topics-page.html', context)

def search_page(request):

    if request.method == 'GET':

        search_query = request.GET.get('search_word')

        if not search_query or search_query.strip() == "":
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        related_questions = QuestionThread.objects.filter(
            Q(title__icontains=search_query) |
            Q(body__icontains=search_query) |
            Q(topic__name__icontains=search_query) |
            Q(created_by__username__icontains=search_query)
        )

        context = {
            'related_questions': related_questions,
            'search_query': search_query,
            'total_related_questions': len(related_questions),
        }

        return render(request, 'section/search-page.html', context)

    return redirect(request.META.get('HTTP_REFERER', '/'))

def explore_topics(request):
    topics = Topic.objects.all()

    context = {
        'topics': topics,
    }

    return render(request, 'section/explore-topics-page.html', context)