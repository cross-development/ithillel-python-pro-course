"""
Forms for the application.

This module defines the forms used in the application.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user with username, email, and password.

    Attributes:
        email (EmailField): The email address of the user, required and unique.
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    """
    Form for authenticating a user with username and password.
    """

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
