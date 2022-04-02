from django.http import HttpRequest
from django.shortcuts import render
from api.models import Task

# Create your views here.
def home(req: HttpRequest):
    return render(req, "home.html")

def todo_add(req: HttpRequest):
    tasks = Task.objects.all()
    print(tasks)
    context = {"tasks": tasks}
    return render(req, "todolist.html", context)

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
