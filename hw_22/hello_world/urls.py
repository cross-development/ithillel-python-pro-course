"""
Module for user-related URL configurations.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('users/', views.user_list, name='user_list'),
]
