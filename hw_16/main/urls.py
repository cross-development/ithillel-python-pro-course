"""
URL configuration for the main application.

This module defines URL patterns for the main app, mapping views to their respective routes.
"""

from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns: list[URLPattern] = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('services/', views.ServiceView.as_view(), name='services'),
]
