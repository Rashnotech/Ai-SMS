from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .serializers import ServerSerializer
from .models import Server
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
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
            return Response(
                {'message': 'Server added successfully.'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'error': 'Data is not valid.'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(
            {'error': 'Method not allowed.'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


@api_view(['GET'])
def get_server(request):
    """a function that get all the information about server"""
    server = Server.objects.all()
    serializer = ServerSerializer(server, many=True)
    return JsonResponse({'my_server': serializer.data})


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
