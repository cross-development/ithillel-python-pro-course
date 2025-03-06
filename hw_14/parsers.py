"""
NewsParser module for extracting structured news data from HTML.

This module defines:
- An abstract base class `NewsParser` for parsing news.
- A specific implementation `SkyNewsParser` for Sky News.
- A `NewsParserFactory` to create appropriate parser instances.
"""

from datetime import datetime
from typing import Dict, List
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from hw_14.logger import logging
from hw_14.config import Config, NewsSource

logger = logging.getLogger(__name__)


class NewsParser(ABC):
    """
    Abstract base class for parsing news from HTML content.

    Attributes:
        _config (Config): Configuration instance containing site-specific settings.
    """

    def __init__(self) -> None:
        """
        Initializes the NewsParser with configuration settings.
        """

        self._config = Config()

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> List[Dict]:
        """
        Parses the provided BeautifulSoup object and extracts news articles.

        Args:
            soup (BeautifulSoup): The parsed HTML content.

        Returns:
            List[Dict]: A list of dictionaries, each representing a news article.
        """


class SkyNewsParser(NewsParser):
    """
    A concrete parser for extracting news articles from Sky News.

    This class includes error handling for cases where articles or individual elements
    are not found in the HTML structure.
    """

    def parse(self, soup: BeautifulSoup) -> List[Dict]:
        """
        Extracts news articles from the given BeautifulSoup object.

        Args:
            soup (BeautifulSoup): The parsed HTML content.

        Returns:
            List[Dict]: A list of dictionaries containing 'title', 'link', 'date', and 'summary'.

        Notes:
            Handles cases where articles or individual elements (title, link, date, summary)
            are not found, logging warnings and using fallback values.
        """

        news_list = []
        articles = soup.find_all("article", class_="ui-story")

        if not articles:
            logger.warning("No articles found with class 'ui-story'. Check the website structure.")
            return news_list

        for article in articles:
            try:
                title_elem = article.find("a", class_="ui-story-headline")

                if not title_elem:
                    logger.warning("Title element not found in article. Using fallback 'No title'.")
                    title = "No title"
                else:
                    title = title_elem.text.strip()

                link_elem = article.find("a", class_="ui-story-headline")

                if not link_elem or "href" not in link_elem.attrs:
                    logger.warning("Link element not found or missing href attribute. Using empty link.")
                    link = ""
                else:
                    link = link_elem["href"]
                    if link and not link.startswith("http"):
                        link = self._config.base_url + link

                date_elem = article.find("time", class_="ui-story-timestamp")

                if not date_elem or "datetime" not in date_elem.attrs:
                    logger.warning("Date element not found or missing datetime attribute. Using current date.")
                    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                else:
                    date = date_elem["datetime"]

                summary_elem = article.find("p", class_="ui-story-description")

                if not summary_elem:
                    logger.warning("Summary element not found in article. Using fallback 'No summary'.")
                    summary = "No summary"
                else:
                    summary = summary_elem.text.strip()

                news_list.append({"title": title, "link": link, "date": date, "summary": summary})

            except AttributeError as e:
                logger.error(f"Unexpected error processing article: {e}. Skipping this article.")
                continue  # Skip current article and move on to the next one

        return news_list


class NewsParserFactory(ABC):
    """
    Factory class for creating appropriate NewsParser instances based on the site name.
    """

    @staticmethod
    def create_parser(site_name: str) -> NewsParser:
        """
        Returns a parser instance for the given site.

        Args:
            site_name (str): The name of the news site.

        Returns:
            NewsParser: An instance of the corresponding parser.

        Raises:
            NotImplementedError: If no parser is implemented for the given site.
        """

        if site_name == NewsSource.SKY_NEWS.value.name:
            return SkyNewsParser()

        raise NotImplementedError(f"Parser for site '{site_name}' is not implemented")
