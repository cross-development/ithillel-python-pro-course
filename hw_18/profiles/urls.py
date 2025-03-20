"""
URL configuration for the application.

This module defines URL patterns for the app, mapping views to their respective routes.
"""

from django.urls import path

from .views import RegisterView, EditProfileView, ChangePasswordView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
