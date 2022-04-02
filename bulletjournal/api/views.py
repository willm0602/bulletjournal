from os import access
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect

from .utils import random_str
from .models import Habit, User, Task

# Create your views here.
def new_user(req: HttpRequest):
    try:
        data = req.POST
        username = data.get('username')
        password = data.get('password')
        access_token = random_str(128)
        req.session["access"] = access_token
        
        user: User = User.objects.create(
            username=username,
            password=password,
            access_token=access_token
        )
        user.save()
        
        return redirect('/')
    
    except Exception as e:
        print(e)
        return redirect('/signup')
   
    
def login_attempt(req: HttpRequest):
    data = req.GET
    username = data.get('username')
    password = data.get('password')
    user = User.objects.get(username=username)
    if user and user.password == password:
        req.session["access"] = user.access_token
        return redirect('/')
    return redirect('/login')

<<<<<<< HEAD

def new_habit(req: HttpRequest):
    data = req.POST
    user: User = get_object_or_404(User, access_token=data.get('access'))
    habit = Habit.objects.create(
        user=user,
        name=data.get('name')
    )
    habit.save()
    
    return redirect('/habits')
=======
def new_todo_item(req: HttpRequest):
    data = req.POST
    task_name = data.get('task_name') # task_name is the the <name> of the input text

    task: Task = Task.objects.create(
        task_text=task_name, # task_text is the name of the text field
        completed=False 
    )

    task.save()

    

    return redirect("/todo")

        #     user: User = User.objects.create(
        #     username=username,
        #     password=password,
        #     access_token=access_token
        # )
        # user.save()
        
        # return redirect('/')

    # username = data.get('username')
    # password = data.get('password')
    # access_token = random_str(128)
    # req.session["access"] = access_token

    
>>>>>>> 0a3ee6e5912a84f62f7a99fafa5177cdbd5e9bf0
