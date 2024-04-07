#!/usr/bin/env python3
"""a module than handles app url"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path('register', views.register)
]