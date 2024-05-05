"""a module that handle user authentication/validation"""
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegister, AuthenticationForm


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
