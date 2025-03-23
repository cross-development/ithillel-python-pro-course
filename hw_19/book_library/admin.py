"""
Admin configuration for the application.

This module registers models for the Django admin interface.
"""

from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest

from .models import Book


class BookAdmin(admin.ModelAdmin):
    """
    Admin interface for Book model
    """

    list_display = ("title", "author", "publication_year", "user")
    search_fields = ("title", "author")
    list_filter = ("genre", "publication_year", "user")
    readonly_fields = ("created_at", "user")

    def save_model(self, request: HttpRequest, obj: Book, form: ModelForm, change: bool) -> None:
        """
        Automatically sets the user field for new objects before saving.

        Args:
            request (HttpRequest): The HTTP request instance.
            obj (Book): The Book instance being saved.
            form (ModelForm): The model form instance.
            change (bool): Indicates whether the object is being updated (True) or created (False).
        """

        if not change:
            obj.user = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Book, BookAdmin)
