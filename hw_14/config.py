"""
Configuration Module.

This module defines the configuration settings for a news scraping application.
It includes an enumeration for news sources and a singleton configuration class.
"""

from enum import Enum
from collections import namedtuple

# Define a named tuple to store news source data
SourceData = namedtuple("SourceData", ["name", "url"])


class NewsSource(Enum):
    """
    Enumeration of available news sources.

    Attributes:
        SKY_NEWS (SourceData): Represents Sky News with its name and base URL.
    """

    SKY_NEWS = SourceData("sky_news", "https://news.sky.com")


class Config:
    """
    Singleton class for application configuration.

    This class ensures that only one instance of the configuration exists
    throughout the application lifecycle.
    """

    _instance = None

    def __new__(cls, *args, **kwargs) -> "Config":
        """
        Creates and returns a singleton instance of the Config class.

        Returns:
            Config: The single instance of the Config class.
        """

        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self) -> None:
        """
        Initializes the configuration with default values.
        """

        self.site_name = NewsSource.SKY_NEWS.value.name
        self.base_url = NewsSource.SKY_NEWS.value.url
        self.days_to_filter = 7
