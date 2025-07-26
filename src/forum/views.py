from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import QuestionThread


def homepage_view(request):

    question_thread = QuestionThread.objects.all()[:5]
    context = {
        'question_thread': question_thread,
    }

    return render(request, 'home.html', context)


@login_required(login_url='auth/login/')
def enter_room(request, room_id):

    question_thread = QuestionThread.objects.get(id=room_id)

    context = {
        'question_thread': question_thread
    }

    return render(request, 'section/room.html', context)