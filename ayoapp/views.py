from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'ayoapp/home.html')

def myexperience(request):
    return render(request, 'ayoapp/myexperience.html')