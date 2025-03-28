"""
Models for the books app.

This module defines the data models for the book library system.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model that extends AbstractUser with a unique email field.

    Attributes:
        email (str): The email address of the user, must be unique.
    """

    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural= "Users"
