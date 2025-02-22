"""Data models for user session."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserSession:
    """Represents a user session model."""

    user_id: str
    session_token: str
    login_time: datetime

    def __str__(self) -> str:
        """
        Returns a string representation of the UserSession object.

        Returns:
            str: A sort information about the user session object.
        """

        return f"User ID: {self.user_id}, login time: {self.login_time.strftime('%Y-%m-%d %H:%M')}"
