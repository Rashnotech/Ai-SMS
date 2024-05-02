#!/usr/bin/env python3
"""a module than handles app url"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("app", views.app),
    path("dashboard", views.dashboard),
    path("services", views.services),
    path("firewall", views.firewall),
    path("network", views.network),
    path("app/profile", views.profile),
    path("app/settings", views.settings)
]
