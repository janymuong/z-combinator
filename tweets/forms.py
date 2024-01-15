# tweets/forms.py
from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2')