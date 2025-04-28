"""
Django URL routing for the chat app.

This module defines the URL patterns for the chat application, including views for listing
rooms, registering users, and retrieving room details. It also includes an API view for async room listings.
"""

from django.urls import path

from .views import RoomListView, RoomDetailView, RoomListAsyncAPIView, RegisterView

app_name = 'chat'

urlpatterns: list = [
    path('', RoomListView.as_view(), name='room-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/rooms/', RoomListAsyncAPIView.as_view(), name='room-list-async'),
    path('room/<str:room_name>/', RoomDetailView.as_view(), name='room-detail'),
]
