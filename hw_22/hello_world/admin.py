"""
Admin configuration for the application.

This module registers models for the Django admin interface.
"""

from django.contrib import admin

from .models import User

admin.site.register(User)
