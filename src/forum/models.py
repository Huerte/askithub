from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuestionThread(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=1000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Room: {self.created_by.username} - {self.topic}'
    
    def placeholder_paragraph(self):
        return self.body[:50]
    
    def answers_count(self):
        return self.answers.count()

class Answer(models.Model):
    answer_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000)
    question = models.ForeignKey(QuestionThread, on_delete=models.CASCADE, related_name='answers')

    answer_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Answer: {self.answer_by.username}'