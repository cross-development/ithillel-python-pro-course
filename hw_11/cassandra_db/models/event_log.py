"""
Data models for event logs.
"""

from uuid import UUID
from datetime import datetime
from dataclasses import dataclass


@dataclass
class EventLog:
    """
    Represents an event log model.
    """

    event_id: UUID
    user_id: str
    event_type: str
    metadata: str
    timestamp: datetime

    def __str__(self) -> str:
        """
        Returns a string representation of the EventLog model.

        Returns:
            str: String representation of the event log model.
        """

        return (f"Event ID: {self.event_id}, "
                f"user ID: {self.user_id}, "
                f"event type: {self.event_type}, "
                f"date: {self.timestamp.strftime('%Y-%m-%d %H:%M')}, "
                f"metadata: {self.metadata}")
