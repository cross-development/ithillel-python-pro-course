"""Repository for managing user sessions in Redis."""

import json
from datetime import datetime

from hw_11.redis_db.redis_client import RedisClient
from hw_11.redis_db.models import UserSession
from hw_11.redis_db.config import SESSION_TTL


class SessionRepository:
    """Handles CRUD operations for user sessions in Redis."""

    def __init__(self) -> None:
        """Initialize Redis client instance."""

        self.client = RedisClient().get_client()

    def create_session(self, session: UserSession) -> None:
        """Create a new user session.

        Args:
            session (UserSession): The session object to store.
        """

        session_data = {
            "session_token": session.session_token,
            "login_time": session.login_time.isoformat(),
        }

        self.client.setex(f"session:{session.user_id}", SESSION_TTL, json.dumps(session_data))

    def get_session(self, user_id: str) -> UserSession | None:
        """Retrieve an active session for a user.

        Args:
            user_id (str): The user ID.

        Returns:
            UserSession | None: The session object if found, otherwise None.
        """

        session_data = self.client.get(f"session:{user_id}")

        if not session_data:
            return None

        data = json.loads(session_data)

        return UserSession(
            user_id=user_id,
            session_token=data["session_token"],
            login_time=datetime.fromisoformat(data["login_time"]),
        )

    def update_session_activity(self, user_id: str) -> None:
        """Update the session's last activity time.

        Args:
            user_id (str): The user ID.
        """

        session = self.get_session(user_id)

        if not session:
            return None

        session.login_time = datetime.now()

        return self.create_session(session)

    def delete_session(self, user_id: str) -> None:
        """Delete a user session.

        Args:
            user_id (str): The user ID.
        """

        self.client.delete(f"session:{user_id}")
