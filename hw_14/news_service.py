"""
NewsService module for fetching, parsing, filtering, and storing news.

This class orchestrates the entire news processing workflow, including:
- Fetching raw news data from a URL.
- Parsing the extracted content.
- Filtering news items based on a given strategy.
- Storing the results in a chosen storage system.
- Generating and logging news statistics.
"""

from typing import Dict, List

import pandas as pd
from tabulate import tabulate

from hw_14.logger import logging
from hw_14.storages import Storage
from hw_14.parsers import NewsParser
from hw_14.fetchers import PageFetcher
from hw_14.filters import FilterStrategy

logger = logging.getLogger(__name__)


class NewsService:
    """
    A service that processes news articles by fetching, parsing, filtering, and storing them.
    """

    def __init__(self, fetcher: PageFetcher, parser: NewsParser,
                 filter_strategy: FilterStrategy, storage: Storage) -> None:
        """
        Initializes the NewsService with required components.

        Args:
            fetcher (PageFetcher): The page fetcher.
            parser (NewsParser): The news parser.
            filter_strategy (FilterStrategy): The filtering strategy.
            storage (Storage): The storage mechanism.
        """

        self.fetcher = fetcher
        self.parser = parser
        self.filter_strategy = filter_strategy
        self.storage = storage

    def process_news(self, url: str) -> None:
        """
        Fetches, parses, filters, and stores news from the given URL.

        Args:
            url (str): The URL to fetch news from.
        """

        soup = self.fetcher.fetch(url)
        news_data = self.parser.parse(soup)

        if not news_data:
            logger.info("Could not find any news.")
            return

        filtered_news = self.filter_strategy.filter(news_data)
        self.storage.save(filtered_news)
        self._generate_stats(filtered_news)

    def _generate_stats(self, news_list: List[Dict]) -> None:
        """
        Generates and logs statistics about the filtered news.

        Args:
            news_list (List[Dict]): The list of filtered news items.
        """

        if not news_list:
            logger.info("No news to analyze.")
            return

        df = pd.DataFrame(news_list)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)

        daily_stats = df.resample('D').size().reset_index(name='count')

        logger.info("News statistics:")
        logger.info(f"Total news: {len(df)}")

        if not daily_stats.empty:
            table = tabulate(daily_stats.values, headers=["Date", "Count"], tablefmt="grid")
            logger.info("Number of news by day:\n" + table)
        else:
            logger.info("There is no data on news in recent days.")

        logger.info("Latest 3 news:")

        for news in news_list[:3]:
            logger.info(f"- {news['title']}")
