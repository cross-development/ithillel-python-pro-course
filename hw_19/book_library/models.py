"""
Models for the books app.

This module defines the data models for the book library system.
"""

from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        genre (str): The genre of the book.
        publication_year (int): The year when the book was published.
        created_at (datetime): Timestamp when the book record was created.
        user (User): The user who added this book to the system.
    """

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        """
        Returns a string representation of the book.

        Returns:
            str: The title of the book.
        """

        return self.title
