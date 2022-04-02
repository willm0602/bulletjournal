from os import access
from django.http import HttpRequest
from django.shortcuts import render
from api.models import Habit

# Create your views here.
def home(req: HttpRequest):
    print(req.session.items())
    return render(req, "home.html", context={
        "access_token": req.session.get("access")
    })

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
    context = {"access": access}
    return render(req, "habits.html", context)