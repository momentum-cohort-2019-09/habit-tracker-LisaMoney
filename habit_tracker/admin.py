from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from habit_tracker.models import User, Habit, History, Comment

# Register your models here.

class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'name',
        'goal',
        'created_date',
        'end_date',
    )
admin.site.register(User, UserAdmin)
admin.site.register(Habit)
admin.site.register(History)
admin.site.register(Comment)
