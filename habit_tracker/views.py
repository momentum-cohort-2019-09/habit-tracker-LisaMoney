from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, History, Comment
from habit_tracker.forms import HabitForm
from django.utils import timezone

# Create your views here.

@csrf_exempt
def home_page(request):
    user = request.user
    return render(request, 'home.html', {"user": user})

def habit_page(request):
    user = request.user
    if request.method=='POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False) 
            habit.user = request.user
            habit.created_at = timezone.now()
            habit.save()
            return redirect('/')
    else:
        form = HabitForm()
    return render(request, 'add_habit.html', {
        'form': form
    })

    return render(request, 'home.html')

