from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QuestionThread, Answer, Topic


def homepage_view(request):

    question_thread = QuestionThread.objects.all()[:5]
    context = {
        'question_thread': question_thread,
    }

    return render(request, 'home.html', context)


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