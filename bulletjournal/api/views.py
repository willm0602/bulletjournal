from django.http import HttpRequest
from django.shortcuts import redirect
from .models import User

# Create your views here.
def new_user(req: HttpRequest):
    try:
        data = req.POST
        username = data.get('username')
        password = data.get('password')
        
        user: User = User.objects.create(
            username=username,
            password=password
        )
        user.save()
        
        return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/signup')