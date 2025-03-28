"""
Module for user-related URL configurations.
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginForm
from .views import RegisterView, DashboardView, SearchView

urlpatterns: list = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('search/', SearchView.as_view(), name='search'),
]
