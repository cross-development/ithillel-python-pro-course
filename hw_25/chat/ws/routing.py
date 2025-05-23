"""
URL routing for WebSocket connections in the chat application.
"""

from django.urls import re_path

from chat.ws import consumers

websocket_urlpatterns = [
    re_path(r'ws/room/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]
