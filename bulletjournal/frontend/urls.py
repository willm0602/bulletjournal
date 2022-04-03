from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('signup', views.signup),
    path('login', views.login),
    path('habits', views.habit_tracker),
    path('todo', views.todo_add),
    path('cal', views.get_cal),
    # path('mark_done', views.mark_done),
]
