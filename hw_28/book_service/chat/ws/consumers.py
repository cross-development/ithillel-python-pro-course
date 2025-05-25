"""
WebSocket consumer for handling real-time chat functionality.
"""

from django.contrib.auth.models import AnonymousUser, User
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from chat.models import Room


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """
    WebSocket consumer allowing only authenticated room participants.
    """

    async def connect(self) -> None:
        """
        Handles the WebSocket connection. Ensures that the user is authenticated
        and is a participant in the room.
        """

        user: User = self.scope.get('user', AnonymousUser())

        if not user.is_authenticated:
            await self.close()
            return

        self.room_name: str = self.scope['url_route']['kwargs']['room_name']

        is_participant = await self._is_participant(user, self.room_name)

        if not is_participant:
            await self.close()
            return

        self.group_name: str = f'room_{self.room_name}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code: int) -> None:
        """
        Handles the WebSocket disconnection.

        Args:
            code (int): The disconnection code.
        """

        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content: dict, **kwargs) -> None:
        """
        Receives JSON messages from the WebSocket.

        Args:
           content (dict): The content of the received JSON message.
           kwargs: Additional arguments.
        """

        message: str = content.get('message', '')

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'username': self.scope['user'].username,
                'message': message,
            }
        )

    async def chat_message(self, event: dict) -> None:
        """
        Sends a chat message to the WebSocket.

        Args:
            event (dict): The event containing the message data.
        """

        await self.send_json({
            'username': event['username'],
            'message': event['message'],
        })

    @database_sync_to_async
    def _is_participant(self, user: User, room_name: str) -> bool:
        """
        Checks if a user is a participant in the specified room.

        Args:
            user (User): The user to check.
            room_name (str): The room name.

        Returns:
            bool: True if the user is a participant, False otherwise.
        """

        try:
            room = Room.objects.get(name=room_name)
        except Room.DoesNotExist:
            return False
        return room.participants.filter(pk=user.pk).exists()
