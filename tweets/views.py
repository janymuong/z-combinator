# tweets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tweet, UserProfile
from .forms import TweetForm

@login_required
def home(request):
    tweets = Tweet.objects.all()
    form = TweetForm()

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            
            # Access the user profile directly from request.user
            new_tweet.user = request.user
            
            new_tweet.save()
            return redirect('home')

    return render(request, 'tweets/home.html', {'tweets': tweets, 'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

