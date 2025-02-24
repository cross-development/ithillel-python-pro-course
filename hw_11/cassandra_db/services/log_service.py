"""
Service layer for event log management.
"""

from typing import List
from uuid import UUID, uuid4
from datetime import datetime, UTC

from hw_11.cassandra_db.models.event_log import EventLog
from hw_11.cassandra_db.repositories.log_repository import LogRepository


class LogService:
    """
    Provides high-level operations for event logs.
    """

    def __init__(self) -> None:
        """
        Initialize log repository.
        """

        self.repository = LogRepository()

    def log_event(self, user_id: str, event_type: str, metadata: str) -> EventLog:
        """
        Create a new event log.

        Args:
            user_id (str): The user ID.
            event_type (str): The type of event.
            metadata (str): Additional event data.

        Returns:
            EventLog: The created event log.
        """

        log = EventLog(
            event_id=uuid4(),
            user_id=user_id,
            event_type=event_type,
            metadata=metadata,
            timestamp=datetime.now(UTC),
        )

        self.repository.insert_log(log)

        return log

    def get_recent_events(self, event_type: str) -> List[EventLog]:
        """
        Retrieve recent events of a specific type.

        Args:
            event_type (str): The event type.

        Returns:
            List[EventLog]: List of event logs.
        """

        return self.repository.get_logs_by_type(event_type)

    def get_event_by_id(self, event_id: UUID) -> EventLog | None:
        """
        Retrieve the event by event id.

        Args:
            event_id (UUID): The event ID.

        Returns:
            EventLog | None: The event log if found.
        """

        return self.repository.get_log_by_event_id(event_id)

    def update_event_metadata(self, event_id: UUID, new_metadata: str) -> None:
        """
        Update event metadata.

        Args:
            event_id (UUID): The event ID.
            new_metadata (str): The updated metadata.
        """

        self.repository.update_metadata(event_id, new_metadata)

    def clean_old_logs(self) -> None:
        """
        Remove logs older than the retention period.
        """

        self.repository.delete_old_logs()
