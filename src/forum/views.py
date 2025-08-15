from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QuestionThread, Answer, Topic
from django.http import JsonResponse
from accounts.views import update_user_status
from accounts.models import UserActivity


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

        user_activity = UserActivity.objects.create(
            user=request.user,
            activity_type=UserActivity.ANSWER_CREATED,
            answer=answer,
            question=question,
        )
        user_activity.save()

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

        user_activity = UserActivity.objects.create(
            user=request.user,
            activity_type=UserActivity.QUESTION_CREATED,
            question=new_question,
        )
        user_activity.save()


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
