"""
Filters for the books app.

This module defines the filters used for filtering and searching books.
"""

import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    """
    FilterSet for Book model.

    Allows filtering books by author, genre, publication_year, and searching by title.
    """

    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('author', 'genre', 'publication_year')
