from django.db import models
from django.contrib.auth.models import User


class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'