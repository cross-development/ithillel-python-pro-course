"""
Admin configuration for the application.

This module registers models for the Django admin interface.
"""

from django.contrib import admin

from .models import User, Comment, Ad, Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin interface for User model.
    """

    list_display = ('username', 'email', 'phone_number', 'address')
    search_fields = ('username', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Category model.
    """

    list_display = ('name', 'active_ads_count')
    readonly_fields = ('active_ads_count',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Admin interface for Ad model.
    """

    list_display = ('title', 'user', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for Comment model.
    """

    list_display = ('ad', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)
