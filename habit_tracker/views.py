from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, History, Comment

# Create your views here.

@csrf_exempt
def home_page(request):
    user = request.user
    return render(request, 'home.html', {"user": user})

def profile_page(request, pk):
    return render(request, 'profile.html')