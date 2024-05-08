"""a module that handle user authentication/validation"""
from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegister, AuthenticationForm
from django.contrib.auth import logout


def register(request):
    """a function that register user"""
    User = get_user_model()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist, please use a different email')
            else:
                user = form.save(commit=False)
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']

                if password1 == password2:
                    user.set_password(password1)
                    user.save()
                    messages.success(request, f'Registered successfully')
                    return redirect('/login')
    else:
        form = UserRegister()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['user_email'] = user.email
            return redirect('/app')
    else:
        form = AuthenticationForm(request)
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login')
