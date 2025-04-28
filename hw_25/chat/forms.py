"""
Forms for the application.

This module defines the forms used in the application.
"""

from typing import Dict, Any

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Room


class RoomForm(forms.ModelForm):
    """
    Form for creating a chat room.
    """

    class Meta:
        model = Room
        fields = ['name']


class RegistrationForm(forms.Form):
    """
    A form for registering a new user.

    Attributes:
        username (CharField): The username.
        email (EmailField): The email address.
        password (CharField): The password.
        password_confirm (CharField): Password confirmation.
    """

    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    def clean_username(self) -> str:
        """
        Validates that the username is unique.

        Raises:
            ValidationError: If the username is already taken.

        Returns:
            str: The validated username.
        """

        username: str = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken")

        return username

    def clean_email(self) -> str:
        """
        Validates that the email is unique.

        Raises:
            ValidationError: If the email is already in use.

        Returns:
            str: The validated email.
        """

        email: str = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use")

        return email

    def clean(self) -> Dict[str, Any]:
        """
        Validates that the passwords match.

        Raises:
            ValidationError: If the passwords do not match.

        Returns:
            Dict[str, Any]: Cleaned form data.
        """

        cleaned_data: Dict[str, Any] = super().clean()
        password: str = cleaned_data.get("password")
        password_confirm: str = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise ValidationError("Passwords do not match")

        return cleaned_data
