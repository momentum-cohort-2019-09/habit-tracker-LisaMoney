# {% load static %}

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    name=models.CharField(max_length=255)
    goal=models.IntegerField()
    start_date=models.DateField(default=timezone.now)
    user=models.ForeignKey(to='User', on_delete=models.CASCADE, blank=False, related_name='author')
    end_date=models.DateTimeField(default=timezone.now)
    description=models.CharField(max_length=255)
    observer=models.ManyToManyField(to='User', related_name='habits_observing', blank=True)
    def __str__(self):
        return self.name

class History(models.Model):
    daily_input=models.TextField()
    met_goal=models.BooleanField(default=False)
    date=models.DateTimeField(default=timezone.now)
    habit=models.ForeignKey(to=Habit, on_delete=models.CASCADE, blank=False, related_name='practice')
    def __str__(self):
        return self.habit 

    
