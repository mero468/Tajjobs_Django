from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'pages/Home.html')

def terms(request):
    return render(request,'pages/Terms.html')

def privacy(request):
    return render(request, 'pages/Privacy.html')

def login(request):
    return render(request, 'pages/Login.html')

def signup(request):
    return render(request, 'pages/signup.html')