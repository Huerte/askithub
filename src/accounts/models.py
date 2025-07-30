from django.db import models
from django.contrib.auth.models import User


class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' ' + 'Online' if self.is_online else 'Offline'