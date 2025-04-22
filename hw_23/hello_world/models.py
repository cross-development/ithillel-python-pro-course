"""
Models for the books app.

This module defines the data models for the application.
"""

from django.db import models


class User(models.Model):
    """
    Represents a user in the application.

    Attributes:
        name (str): The full name of the user.
        email (str): The email address of the user.
        avatar (ImageField): The avatar image of the user.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        """
        Return a string representation of the user.

        Returns:
            str: The user's name.
        """

        return self.name
