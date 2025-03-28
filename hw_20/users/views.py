"""
Views for the application.

This module defines the views used in the application.
"""

from typing import Optional, Dict

from django.db import connection
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistrationForm


class RegisterView(CreateView):
    """
    View for registering a new user.

    Attributes:
        form_class (RegistrationForm): The form class for user registration.
        template_name (str): The template to render for registration.
        success_url (str): URL to redirect to upon successful registration.
    """

    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the dashboard, accessible only to authenticated users.

    Attributes:
        template_name (str): The template to render for the dashboard.
    """

    template_name = 'users/dashboard.html'


def get_user_by_username(username: str) -> Optional[Dict[str, str]]:
    """
    Fetch a user by username using a parameterized raw SQL query.

    Args:
        username (str): The username to search for.

    Returns:
        Optional[Dict[str, str]]: User data if found, None otherwise.
    """

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, username, email FROM users_customuser WHERE username = %s",
            [username]
        )
        row = cursor.fetchone()

    if row:
        return {'id': row[0], 'username': row[1], 'email': row[2]}

    return None


class SearchView(TemplateView):
    template_name = 'users/search.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Handle GET request: display an empty search form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Rendered template with an empty form.
        """

        return render(request, self.template_name)

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Handle POST request: search for a user by the provided username.

        Args:
            request (HttpRequest): The HTTP request object containing the username.

        Returns:
            HttpResponse: Rendered template with search result message.
        """

        username = request.POST.get('username', '')
        user = get_user_by_username(username)
        message = f"User with username \"{username}\" not found."

        if user:
            message = f"User with username \"{username}\" found."

        return render(request, self.template_name, {'message': message})
