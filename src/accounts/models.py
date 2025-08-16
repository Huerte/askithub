from django.db import models
from django.contrib.auth.models import User
from forum.models import QuestionThread, Answer


class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    last_seen = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Status'

    def __str__(self):
        return f'{self.user.username}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    
    following = models.ManyToManyField(
        'self',
        # This symmetrical=False help as achieved 
        # a following/follower feature since 
        # if it true then if A (user) follow B 
        # then django automatically assume that B follow A 
        # which is not what we want
        symmetrical=False, 
        related_name='followers',
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return f'{self.user.username}'


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    FOLLOWED_USER = 'followed_user'
    QUESTION_CREATED = 'question_created'
    ANSWER_CREATED = 'answer_created'

    ACTIVITY_TYPES = [
        (FOLLOWED_USER, 'Followed User'),
        (QUESTION_CREATED, 'Question Created'),
        (ANSWER_CREATED, 'Answer Created'),
    ]

    activity_type = models.CharField(
        max_length=100,
        choices=ACTIVITY_TYPES,
    )

    question = models.ForeignKey(QuestionThread, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

    followed_user = models.ForeignKey(Profile, related_name='follow_activities', on_delete=models.CASCADE, null=True, blank=True)

    # This is a flag used to determine if this history should be shown
    is_active = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Activities'

    def get_activity_type(self):
        return self.get_activity_type_display()
    
    def get_question_display(self):
        if self.question:
            return self.question.body[:30]
        return 'Empty'
    
    def get_answer_display(self):
        if self.answer:
            return self.answer.body[:30]
        return 'Empty'

    def __str__(self):
        return f'{self.user.username} -> {self.get_activity_type_display()}'