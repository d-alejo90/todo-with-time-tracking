from django.shortcuts import render, redirect
from .models import User

def register(request):
    context = {}
    return render(request, 'authentication/register.html', context)

def signin(request):
    context = {}
    return render(request, 'authentication/login.html', context)