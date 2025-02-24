"""
Configuration settings for connecting to Cassandra.
"""

from typing import List

CASSANDRA_HOSTS: List[str] = ["127.0.0.1"]
CASSANDRA_KEYSPACE: str = "event_logs"
CASSANDRA_TABLE: str = "logs"
LOG_RETENTION_DAYS: int = 7
