"""
Singleton for MongoDB connection.
"""

from pymongo import MongoClient
from pymongo.database import Database

from hw_11.mongo_db.config import MONGO_DB_NAME, MONGO_URI


class MongoDBClient:
    """
    Singleton class for managing a MongoDB connection.

    This class ensures that only a single instance of the MongoDBClient is created
    throughout the application. It manages the connection to the MongoDB database
    and provides access to the database instance.
    """

    _instance = None

    def __new__(cls) -> "MongoDBClient":
        """
        Ensures only one instance of MongoDBClient exists.

        This method implements the Singleton design pattern to create and return
        the single instance of MongoDBClient. If the instance does not exist,
        a new instance is created and initialized with a MongoDB client connection.

        Returns:
            MongoDBClient: The singleton instance of MongoDBClient.
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(MONGO_URI)
            cls._instance.db = cls._instance.client[MONGO_DB_NAME]

        return cls._instance

    def get_database(self) -> Database:
        """
        Get the MongoDB database instance.

        This method provides access to the MongoDB database instance, which can
        be used to interact with the database collections.

        Returns:
            Database: The MongoDB database instance.
        """

        return self.db
