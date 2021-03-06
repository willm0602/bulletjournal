from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.new_user),
    path("login-attempt", views.login_attempt),
    path("new-habit", views.new_habit),
    path("new_todo_item", views.new_todo_item),
    path("add_date", views.habit_add_date),
    path("remove_date", views.habit_remove_date),
    path("signout", views.signout),
    path("todo_complete", views.todo_complete),
    path("todo_delete", views.todo_remove),
    path("todo_reopen", views.reopen_task)
]
