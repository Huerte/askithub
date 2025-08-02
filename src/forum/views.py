from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QuestionThread, Answer, Topic
from django.db.models import Q


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

    question_thread = QuestionThread.objects.all()

    context = {
        'all_questions': question_thread,
    }

    return render(request, 'section/explore-page.html', context)

@login_required(login_url='/auth/login')
def profile_view(request):
    context = {}
    return render(request, 'section/profile-page.html', context)

@login_required(login_url='/auth/login')
def enter_room(request, room_id):

    question_thread = QuestionThread.objects.get(id=room_id)
    answers = question_thread.answers.all()

    context = {
        'question_thread': question_thread,
        'answers': answers,
    }

    return render(request, 'section/room.html', context)

@login_required(login_url='/auth/login/')
def comment(request, room_id):

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

    comment = get_object_or_404(Answer, id=comment_id)

    if request.user == comment.answer_by:
        comment.delete()

    return redirect(request.META.get('HTTP_REFERER', '/')) # This will return the user to the page he/she come from


@login_required(login_url='/auth/login/')
def add_question(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        body = request.POST.get('body')

        if not title or not topic:
            return redirect('homepage')
        
        topic_instance, _ = Topic.objects.get_or_create(name=topic.title())

        new_question = QuestionThread(created_by=request.user, title=title, topic=topic_instance, body=body)
        new_question.save()
    
    return redirect('homepage')

@login_required(login_url='/auth/login/')
def delete_question(request, room_id):

    room = get_object_or_404(QuestionThread, id=room_id)

    if room.created_by == request.user:
        room.delete()
    
    return redirect('homepage')


@login_required(login_url='/auth/login/')
def edit_answer(request, answer_id):

    if request.method == 'POST':
        body = request.Post.get('body')

        ## Add a edit comment feature

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
