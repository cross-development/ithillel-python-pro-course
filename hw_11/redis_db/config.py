"""Configuration settings for connecting to Redis."""

REDIS_HOST: str = 'localhost'
REDIS_PORT: int = 6379
REDIS_DB: int = 0
SESSION_TTL: int = 1800  # Time-to-live for session (30 minutes)
