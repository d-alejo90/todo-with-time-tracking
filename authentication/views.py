from django.shortcuts import render, redirect, reverse
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import re

def register(request):
    context = {'has_error': False, 'data': request.POST}
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if len(password) < 6:
            messages.add_message(request, messages.ERROR, "Password should be atleast 6 characters")
            context['has_error'] = True
        if password != password2:
            messages.add_message(request, messages.ERROR, "Password mismatch")
            context['has_error'] = True
        if not email:
            messages.add_message(request, messages.ERROR, "Email is required")
            context['has_error'] = True
        if email and not validate_email(email):
            messages.add_message(request, messages.ERROR, "Email is not valid")
            context['has_error'] = True
        if email and User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, "Email is already in use, choose another one")
            context['has_error'] = True
        if not username:
            messages.add_message(request, messages.ERROR, "Username is required")
            context['has_error'] = True
        if username and User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "Username is taken, choose another one")
            context['has_error'] = True
        
        if context['has_error']:
            return render(request, 'authentication/register.html', context)

        user = User.objects.create_user(username = username, email = email)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "User created successfully, you can login now")
        redirect('signin')
        
    return render(request, 'authentication/register.html', context)

def validate_email(email):
    # regex for validating an Email
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    return False

def signin(request):
    context = {'has_error': False, 'data': request.POST}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username:
            messages.add_message(request, messages.ERROR, "Username is required")
            context['has_error'] = True
        if username and not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "Username is wrong")
            context['has_error'] = True
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.add_message(request, messages.ERROR, "We couldn't login, please try again later")
            return render(request, 'authentication/login.html', context)
        else:
            login(request, user)
            return redirect(reverse('home'))
        
    return render(request, 'authentication/login.html', context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('signin')