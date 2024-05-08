#!/usr/bin/env python3
"""a module than handles app url"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.app, name='app'),
    path('add_server', views.add_server, name='add_server_api'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("services", views.services, name='services'),
    path("firewall", views.firewall, name='firewall'),
    path("network", views.network, name='network'),
    path("profile", views.profile, name='profile'),
    path("settings", views.settings, name='settings')
]
