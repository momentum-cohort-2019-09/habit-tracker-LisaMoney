from django import forms
from django.forms import ModelForm
from habit_tracker.models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'goal', 'description']



