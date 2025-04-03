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
    """

    name: models.CharField = models.CharField(max_length=100)
    email: models.EmailField = models.EmailField()

    def __str__(self) -> str:
        """
        Return a string representation of the user.

        Returns:
            str: The user's name.
        """

        return self.name
