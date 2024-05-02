"""a module that handle user authentication/validation"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegister, LoginForm


def register(request):
    """a function that register user"""
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            data = form.cleaned_data.items()
            form.save()
            messages.success(request, f'Registered successfully')
            return redirect('/login')
    else:
        form = UserRegister()
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    """a function that authenticate user"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.items()
            form.save()
            messages.success(request, f'Logged in successfully')
            return redirect('/app')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
