from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
    return render(request, 'pages/home.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    return render(request, 'pages/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    form.add_error(None, 'Invalid username or password')

        elif 'register' in request.POST:
            return HttpResponseRedirect('/register')
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})