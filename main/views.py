from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import ServerSerializer
from rest_framework.decorators import api_view
from rest_framework import status


def index(request):
    return render(request, 'main/index.html')


@api_view(['POST'])
@csrf_exempt
def add_server(request):
    if request.method == 'POST':
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            print(request.user)
            print(request.session['user_email'])
            return JsonResponse(
                {'message': 'Server added successfully.'},
                status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {'error': 'Data is not valid.'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return JsonResponse(
            {'error': 'Method not allowed.'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


@login_required
def app(request):
    user_email = request.session.get('user_email')
    email = user_email.split('@')[0].capitalize() if user_email else ''
    return render(request, 'main/app.html', {'email': email})


@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')


@login_required
def network(request):
    return render(request, 'main/network.html')


@login_required
def firewall(request):
    return render(request, 'main/firewall.html')


@login_required
def services(request):
    return render(request, 'main/services.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


@login_required
def settings(request):
    return render(request, 'main/settings.html')
