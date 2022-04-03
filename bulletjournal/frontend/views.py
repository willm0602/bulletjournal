from os import access
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from api.models import Habit, Task, User
from .utils import get_last_days

# Create your views here.
def home(req: HttpRequest):
    print(req.session.items())
    return render(req, "home.html", context={
        "access_token": req.session.get("access")
    })

def todo_add(req: HttpRequest):
    tasks = Task.objects.all()
    print(tasks)
    context = {"tasks": tasks}
    return render(req, "todolist.html", context)

def get_cal(req: HttpRequest):
    return render(req, "calendar.html")

# def mark_done(req: HttpRequest):
#     req.GET.get(tasks)
#     return render(req, "todolist.html")

# def todo_list(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)

## View examples from poll project
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# # Create your views here.
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def signup(req: HttpRequest):
    return render(req, "signup.html")

def login(req: HttpRequest):
    return render(req, "login.html")

def habit_tracker(req: HttpRequest):
    access = req.session.get('access')
    user = User.objects.get(access_token=access)
    habits = Habit.objects.filter(user=user)
    days = get_last_days(7)
    context = {"access": access, "habits": habits, "days": days}
    print(days)
    return render(req, "habits.html", context)