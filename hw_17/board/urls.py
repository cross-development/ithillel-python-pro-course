"""
URL configuration for the application.

This module defines URL patterns for the app, mapping views to their respective routes.
"""

from django.urls import path

from .views import HomeView, CategoryAdsView, AdDetailView, UserAdsView, statistics_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:pk>/', CategoryAdsView.as_view(), name='category_ads'),
    path('user/<int:user_id>/ads/', UserAdsView.as_view(), name='user_ads'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('statistics/', statistics_view, name='admin_statistics'),
]
