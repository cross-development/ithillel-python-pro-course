"""
Django model for chat rooms.

This module defines the 'Room' model, representing a chat room, and its related fields.
The model includes a name for the room and a many-to-many relationship with participants (users).
"""

from django.db import models
from django.contrib.auth import get_user_model


class Room(models.Model):
    """
    Model representing a chat room.

    This model defines a chat room with a unique name and participants. The participants
    are related through a many-to-many relationship with the User model.
    """

    name: str = models.CharField(max_length=255, unique=True)
    participants = models.ManyToManyField(get_user_model(), related_name='rooms', blank=True)

    def __str__(self) -> str:
        """
        Return the string representation of the Room instance.

        Returns:
            str: The name of the room.
        """
        return self.name
