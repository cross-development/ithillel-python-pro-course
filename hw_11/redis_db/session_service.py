"""Service layer for user session management."""

from datetime import datetime

from hw_11.redis_db.session_repository import SessionRepository
from hw_11.redis_db.models import UserSession
from hw_11.redis_db.utils import generate_session_token


class SessionService:
    """Provides high-level operations for user sessions."""

    def __init__(self) -> None:
        """Initialize a session repository."""

        self.repository = SessionRepository()

    def create_user_session(self, user_id: str) -> UserSession:
        """Create a new user session.

        Args:
            user_id (str): The user ID.

        Returns:
            UserSession: The created session.
        """

        session_token = generate_session_token()
        login_time = datetime.now()
        session = UserSession(user_id=user_id, session_token=session_token, login_time=login_time)
        self.repository.create_session(session)

        return session

    def get_user_session(self, user_id: str) -> UserSession | None:
        """Get an active session for the user.

        Args:
            user_id (str): The user ID.

        Returns:
            UserSession | None: The user session if found.
        """

        return self.repository.get_session(user_id)

    def update_user_activity(self, user_id: str) -> None:
        """Update last activity time for a user's session.

        Args:
            user_id (str): The user ID.
        """

        self.repository.update_session_activity(user_id)

    def logout_user(self, user_id: str) -> None:
        """Remove user's session (logout).

        Args:
            user_id (str): The user ID.
        """

        self.repository.delete_session(user_id)
