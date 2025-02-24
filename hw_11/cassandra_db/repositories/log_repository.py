"""
Repository for managing event logs in Cassandra.
"""

from uuid import UUID
from typing import List
from datetime import datetime, timedelta, UTC

from hw_11.cassandra_db.models.event_log import EventLog
from hw_11.cassandra_db.cassandra_client import CassandraClient
from hw_11.cassandra_db.configs.cassandra_config import CASSANDRA_TABLE, LOG_RETENTION_DAYS


class LogRepository:
    """
    Handles CRUD operations for event logs in Cassandra.
    """

    def __init__(self) -> None:
        """
        Initialize Cassandra session.
        """

        self.session = CassandraClient().get_session()
        self._create_table()

    def _create_table(self) -> None:
        """
        Create the logs table if it does not exist.
        """

        self.session.execute(f"""
            CREATE TABLE IF NOT EXISTS {CASSANDRA_TABLE} (
                event_id UUID PRIMARY KEY,
                user_id TEXT,
                event_type TEXT,
                metadata TEXT,
                timestamp TIMESTAMP
            )
        """)

    def insert_log(self, log: EventLog) -> None:
        """
        Insert a new event log.

        Args:
            log (EventLog): The event log object.
        """

        self.session.execute(f"""
            INSERT INTO {CASSANDRA_TABLE} (event_id, user_id, event_type, timestamp, metadata)
            VALUES (%s, %s, %s, %s, %s)
        """, (log.event_id, log.user_id, log.event_type, log.timestamp, log.metadata))

    def get_logs_by_type(self, event_type: str) -> List[EventLog]:
        """
        Retrieve all events of a specific type from the last 24 hours.

        Args:
            event_type (str): The event type to filter logs.

        Returns:
            List[EventLog]: List of event logs.
        """

        time_threshold = datetime.now(UTC) - timedelta(days=1)

        rows = self.session.execute(f"""
            SELECT event_id, user_id, event_type, timestamp, metadata
            FROM {CASSANDRA_TABLE}
            WHERE event_type = %s AND timestamp >= %s
            ALLOW FILTERING
        """, (event_type, time_threshold))

        return [EventLog(row.event_id, row.user_id, row.event_type, row.metadata, row.timestamp)
                for row in rows]

    def get_log_by_event_id(self, event_id: UUID) -> EventLog | None:
        """
        Retrieve the log entry by event id.

        Args:
            event_id (UUID): The event ID.
        Returns:
            EventLog | None: The event log if found.
        """

        rows = self.session.execute(f"""
            SELECT event_id, user_id, event_type, timestamp, metadata
            FROM {CASSANDRA_TABLE}
            WHERE event_id = %s
        """, (event_id,))

        if rows:
            row = rows.one()
            return EventLog(row.event_id, row.user_id, row.event_type, row.metadata, row.timestamp)

        return None

    def update_metadata(self, event_id: UUID, new_metadata: str) -> None:
        """
        Update the metadata for a specific event.

        Args:
            event_id (UUID): The event ID.
            new_metadata (str): The updated metadata.
        """

        self.session.execute(f"""
            UPDATE {CASSANDRA_TABLE} 
            SET metadata = %s 
            WHERE event_id = %s
        """, (new_metadata, event_id))

    def delete_old_logs(self) -> None:
        """
        Delete logs older than the retention period.
        """

        time_threshold = datetime.now(UTC) - timedelta(days=LOG_RETENTION_DAYS)

        rows = self.session.execute(f"""
            SELECT event_id FROM {CASSANDRA_TABLE}
            WHERE timestamp < %s 
            ALLOW FILTERING
        """, (time_threshold,))

        for row in rows:
            self.session.execute(f"""
                DELETE FROM {CASSANDRA_TABLE} WHERE event_id = %s
            """, (row.event_id,))
