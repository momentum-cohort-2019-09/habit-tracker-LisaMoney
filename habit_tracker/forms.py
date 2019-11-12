# {% load static %}

from django import forms
from django.forms import ModelForm
from habit_tracker.models import Habit, History

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ['name', 'goal', 'description']

class InputForm(forms.ModelForm):

    class Meta:
        model = History
        fields = ['daily_input', 'met_goal', 'date']



