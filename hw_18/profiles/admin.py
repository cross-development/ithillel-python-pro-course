"""
Admin configuration for the application.

This module registers models for the Django admin interface.
"""

from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for UserProfile model.
    """

    list_display = ('user', 'birth_date', 'location')
    search_fields = ('user__username',)
