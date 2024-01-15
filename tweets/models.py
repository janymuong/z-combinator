# tweets/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)

class Tweet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
