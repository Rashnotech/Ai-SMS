from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def app(request):
    return render(request, 'main/app.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')
def network(request):
    return render(request, 'main/network.html')
def firewall(request):
    return render(request, 'main/firewall.html')
def services(request):
    return render(request, 'main/services.html')

def profile(request):
    return render(request, 'main/profile.html')

def settings(request):
    return render(request, 'main/settings.html')