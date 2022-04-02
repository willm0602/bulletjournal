from django.urls import path
from . import views

urlpatterns = [
    path('/signup', views.new_user),
    path('/login-attempt', views.login_attempt) ,
    path('/new-habit', views.new_habit)
]
