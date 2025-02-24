"""
Singleton class for Cassandra connection.
"""

from cassandra.cluster import Cluster, Session

from hw_11.cassandra_db.configs.cassandra_config import CASSANDRA_HOSTS, CASSANDRA_KEYSPACE


class CassandraClient:
    """
    Singleton class for managing Cassandra connection.
    """

    _instance = None

    def __new__(cls) -> "CassandraClient":
        """
        Ensure only one instance of CassandraClient exists.
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.cluster = Cluster(CASSANDRA_HOSTS)
            cls._instance.session = cls._instance.cluster.connect()
            cls._instance.session.execute(f"""
                CREATE KEYSPACE IF NOT EXISTS {CASSANDRA_KEYSPACE}
                WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}};
            """)
            cls._instance.session.set_keyspace(CASSANDRA_KEYSPACE)

        return cls._instance

    def get_session(self) -> Session:
        """
        Get Cassandra session instance.

        Returns:
            Session: The Cassandra session.
        """

        return self.session
