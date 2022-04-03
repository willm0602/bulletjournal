from django.contrib import admin
from .models import Habit, User, Task


# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Habit)