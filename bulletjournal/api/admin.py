from django.contrib import admin

from .models import Habit, Task, User

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Habit)
