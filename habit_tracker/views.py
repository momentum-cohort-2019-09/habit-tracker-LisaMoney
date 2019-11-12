# {% load static %}

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, History
from habit_tracker.forms import HabitForm, InputForm
from django.utils import timezone

# Create your views here.

@csrf_exempt
def home_page(request):
    user = request.user
    habits = Habit.objects.all()
    return render(request, 'home.html', {"user": user, "habits": habits})

def profile_page(request):
    user = request.user
    if request.method=='POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False) 
            habit.user = user
            habit = form.save()
            return redirect(to='profile_page')
    else:
        form = HabitForm()
        user_habits = Habit.objects.filter(user=User.objects.get(pk=request.user.pk))
    return render(request, 'profile.html', {
        'form': form, 'user_habits': user_habits, 'user': user
    })

def habit_records(request, pk):
    habit = Habit.objects.get(pk=pk)
    if request.method=='POST':
        form = InputForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False) 
            record.user = request.user
            record.habit = habit
            record.save()
            return redirect(to='habit_records', pk=pk)
    else:
        form = InputForm()
        records = History.objects.filter(habit=habit)
    return render(request, 'habit_records.html', {
        'form': form, 'habit': habit, 'records': records
    })
