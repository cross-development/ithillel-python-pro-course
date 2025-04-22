"""
Views for the application.

This module defines the views used in the application.
"""

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import User


def user_list(request):
    users = User.objects.all()

    return render(request, 'user_list.html', {'users': users})


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, 'hello_world.html')
