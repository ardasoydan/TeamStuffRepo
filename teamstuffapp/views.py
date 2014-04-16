from django.shortcuts import render
from teamstuffapp.models import User,Team,TeamEvent
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    return render(request, 'teamstuffapp/homepage.html')

def signup(request):
    return render(request, 'teamstuffapp/signup.html')

def login(request):
    return render(request, 'teamstuffapp/login.html')

def signin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email = email, password = password)
    if user is not None:
        login(request,user)
        return render(request, 'teamstuffapp/homepage.html',{'email': email})
    else:
        raise ValidationError("login failed")

