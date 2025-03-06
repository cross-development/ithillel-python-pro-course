"""
News Filtering Module.

This module defines an abstract strategy pattern for filtering news data
and a concrete implementation based on date filtering.
"""

from typing import Dict, List
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class FilterStrategy(ABC):
    """
    Abstract base class for filtering news items.

    Subclasses must implement the `filter` method, which processes a list of news items
    and returns a filtered list based on specific criteria.
    """

    @abstractmethod
    def filter(self, news_list: List[Dict]) -> List[Dict]:
        """
        Filters a list of news items based on a specific strategy.

        Args:
            news_list (List[Dict]): A list of news items, where each item is a dictionary.

        Returns:
            List[Dict]: A filtered list of news items.
        """


class DateFilterStrategy(FilterStrategy):
    """
    Filters news items based on their publication date.

    This strategy keeps only the news items that were published within a specified
    number of days from the current date.
    """

    def __init__(self, days: int) -> None:
        """
        Initializes the DateFilterStrategy with a specific time range.

        Args:
            days (int): The number of days within which news should be retained.
        """

        self.days = days

    def filter(self, news_list: List[Dict]) -> List[Dict]:
        """
        Filters the news list, keeping only items published within the last `days` days.

        Args:
            news_list (List[Dict]): A list of news items,
                                    where each item contains at least a 'date' key.

        Returns:
            List[Dict]: A filtered list of news items that fall within the specified time range.
        """

        cutoff_date = datetime.now() - timedelta(days=self.days)

        return [
            news for news in news_list
            if datetime.strptime(news['date'][:10], '%Y-%m-%d') >= cutoff_date
        ]
