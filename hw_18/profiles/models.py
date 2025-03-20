"""
Database models for the application.

This module defines the database models used in the application. Each model
corresponds to a table in the database.
"""

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model representing a user's profile, extending the built-in User model.

    Attributes:
        user (OneToOneField): Link to the User model.
        bio (TextField): User's biography (up to 500 characters).
        birth_date (DateField): User's date of birth.
        location (CharField): User's location.
        avatar (ImageField): User's avatar image.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        """
        Returns the username as a string representation.

        Returns:
            str: The username.
        """

        return self.user.username
