from django.shortcuts import redirect
from django.urls import reverse


class AuthenticationMiddleware:
    """
    A middleware that check if logged otherwise login page
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == reverse('login'):
            return self.get_response(request)
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        return self.get_response(request)
