"""Singleton class for Redis connection"""

import redis

from hw_11.redis_db.config import REDIS_DB, REDIS_HOST, REDIS_PORT


class RedisClient:
    """Singleton class for managing Redis connection."""

    _instance = None

    def __new__(cls) -> "RedisClient":
        """Ensure only one instance of RedisClient exists."""

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = redis.StrictRedis(
                host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True
            )

        return cls._instance

    def get_client(self) -> redis.StrictRedis:
        """Get Redis client instance.

        Returns:
            redis.StrictRedis: The Redis client.
        """

        return self.client
