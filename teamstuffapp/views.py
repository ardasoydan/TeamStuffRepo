from django.shortcuts import render
from teamstuffapp.models import User,Team,TeamEvent

# Create your views here.

def index(request):
    return render(request, 'teamstuffapp/homepage.html')
