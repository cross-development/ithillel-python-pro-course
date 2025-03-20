"""
Forms for the application.

This module defines the forms used in the application.
"""

from typing import Dict, Any, Optional

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile


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


class UserProfileForm(forms.ModelForm):
    """
    A form for editing a user's profile.
    """

    class Meta:
        model = UserProfile
        fields: list = ['bio', 'birth_date', 'location', 'avatar']

    def clean_avatar(self) -> Optional[forms.ImageField]:
        """
        Validates that the avatar size does not exceed 2 MB.

        Raises:
            ValidationError: If the avatar size exceeds 2 MB.

        Returns:
            Optional[ImageField]: The validated avatar.
        """

        avatar: Optional[forms.ImageField] = self.cleaned_data.get('avatar')

        if avatar and avatar.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Avatar file size exceeds 2 MB")

        return avatar


class PasswordChangeForm(forms.Form):
    """
    A form for changing a user's password.

    Attributes:
        current_password (CharField): The current password.
        new_password (CharField): The new password.
        new_password_confirm (CharField): Confirmation of the new password.
    """

    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    new_password_confirm = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, user: Optional[User], *args: Any, **kwargs: Any) -> None:
        """
        Initializes the form with the current user.

        Args:
            user (Optional[User]): The current user.
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """

        self.user: Optional[User] = user
        super().__init__(*args, **kwargs)

    def clean_current_password(self) -> str:
        """
        Validates the current password.

        Raises:
            ValidationError: If the current password is incorrect.

        Returns:
            str: The validated current password.
        """

        current_password: str = self.cleaned_data['current_password']

        if not self.user.check_password(current_password):
            raise forms.ValidationError("Current password is incorrect")

        return current_password

    def clean(self) -> Dict[str, Any]:
        """
        Validates that new passwords match and differ from the current one.

        Raises:
            ValidationError: If new passwords do not match or match the current password.

        Returns:
            Dict[str, Any]: Cleaned form data.
        """

        cleaned_data: Dict[str, Any] = super().clean()
        new_password: str = cleaned_data.get("new_password")
        new_password_confirm: str = cleaned_data.get("new_password_confirm")

        if new_password and new_password_confirm:
            if new_password != new_password_confirm:
                raise forms.ValidationError("New passwords do not match")

            if new_password == cleaned_data.get("current_password"):
                raise forms.ValidationError("New password must be different from the current one")

        return cleaned_data
