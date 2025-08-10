from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QuestionThread, Answer, Topic
from django.db.models import Q
from django.http import JsonResponse
from accounts.views import update_user_status
from django.contrib.auth import get_user_model
from django.db import models


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
    # Get all questions with related data
    question_thread = QuestionThread.objects.select_related('created_by', 'topic').prefetch_related('answers').all().order_by('-created_at')
    
    # Get all topics for filtering
    topics = Topic.objects.all()
    
    # Get some statistics
    total_questions = question_thread.count()
    total_answers = sum(q.answers.count() for q in question_thread)
    total_users = get_user_model().objects.count()
    
    # Get top topics by question count
    top_topics = Topic.objects.annotate(
        question_count=models.Count('questionthread')
    ).order_by('-question_count')[:5]

    context = {
        'all_questions': question_thread,
        'topics': topics,
        'top_topics': top_topics,
        'total_questions': total_questions,
        'total_answers': total_answers,
        'total_users': total_users,
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

@login_required(login_url='/auth/login/')
def comment(request, room_id):
    update_user_status(request)

    if request.method == 'POST':
        comment = request.POST.get('comment')

        if not comment or comment.strip() == "":
            return redirect('enter_room', room_id=room_id)

        question = get_object_or_404(QuestionThread, id=room_id)

        answer = Answer(answer_by=request.user, answer=comment, question=question)
        answer.save()

    return redirect('enter_room', room_id=room_id)

@login_required(login_url='/auth/login/')
def remove_comment(request, comment_id):
    update_user_status(request)

    comment = get_object_or_404(Answer, id=comment_id)

    if request.user == comment.answer_by:
        comment.delete()

    return redirect(request.META.get('HTTP_REFERER', '/')) # This will return the user to the page he/she come from


@login_required(login_url='/auth/login/')
def add_question(request):
    update_user_status(request)

    if request.method == 'POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        body = request.POST.get('body')

        if not title or not topic:
            return redirect('homepage')
        
        topic_instance, _ = Topic.objects.get_or_create(name=topic.title())

        new_question = QuestionThread(created_by=request.user, title=title, topic=topic_instance, body=body)
        new_question.save()

    return redirect(f"{request.META.get('HTTP_REFERER', '/')}?success=1")

@login_required(login_url='/auth/login/')
def delete_question(request, room_id):
    update_user_status(request)
    room = get_object_or_404(QuestionThread, id=room_id)

    if room.created_by == request.user:
        room.delete()
    
    return redirect('homepage')

@login_required(login_url='/auth/login/')
def get_answer_body(request, answer_id):
    update_user_status(request)
    if request.method == 'GET':
        answer = Answer.objects.get(id=answer_id)
        return JsonResponse({'body': answer.answer})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

@login_required(login_url='/auth/login/')
def edit_answer(request, answer_id):
    update_user_status(request)
    if request.method == 'POST':
        body = request.POST.get('body', 'Empty Message...')

        answer = Answer.objects.update_or_create(
            id=answer_id,
            defaults={'answer': body},
        )
        
    return redirect(request.META.get('HTTP_REFERER', '/'))

def visit_topics(request, topic_id):

    topic = get_object_or_404(Topic, id=topic_id)
    questions = QuestionThread.objects.filter(topic=topic)

    context = {
        'questions': questions,
        'topic': topic,
        'total_question': len(questions)
    }

    return render(request, 'section/topics-page.html', context)

def search_page(request):

    if request.method == 'POST':

        search_query = request.POST.get('search_word')

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
