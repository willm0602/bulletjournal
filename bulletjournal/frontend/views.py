from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def home(req: HttpRequest):
    return render(req, "home.html")

def signup(req: HttpRequest):
    return render(req, "signup.html")