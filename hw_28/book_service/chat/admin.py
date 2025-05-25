"""
Django admin configuration for the Room model.

This module registers the Room model with Django's admin interface,
allowing for easy management of Room instances.
"""

from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Room model.

    Customizes how the Room model is displayed and managed in the Django admin interface.
    """

    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('participants',)
