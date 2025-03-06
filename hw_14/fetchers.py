"""
Web Page Fetching Module.

This module defines:
- An abstract `PageFetcher` class for fetching web pages.
- A concrete `RequestsPageFetcher` implementation using `requests` and `BeautifulSoup`.
- Retry logic to handle temporary network failures.
"""

import sys
import time
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup

from hw_14.logger import logging

logger = logging.getLogger(__name__)


class PageFetcher(ABC):
    """
    Abstract base class for fetching web pages.

    Subclasses must implement the `fetch` method to retrieve and parse
    web page content into a BeautifulSoup object.
    """

    @abstractmethod
    def fetch(self, url: str) -> BeautifulSoup:
        """
        Fetches and parses a web page.

        Args:
            url (str): The URL of the web page to fetch.

        Returns:
            BeautifulSoup: A parsed HTML document.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """


class RequestsPageFetcher(PageFetcher):
    """
    Concrete implementation of PageFetcher using the `requests` library.

    This class fetches a web page using an HTTP GET request, parses the
    content with BeautifulSoup, and includes retry logic for failed requests.

    Attributes:
        MAX_RETRIES (int): Maximum number of retry attempts.
        RETRY_DELAY (int): Delay in seconds before retrying a failed request.
    """

    MAX_RETRIES = 3
    RETRY_DELAY = 2

    def fetch(self, url: str) -> BeautifulSoup:
        """
        Fetches and parses a web page using the `requests` library with retry logic.

        Args:
            url (str): The URL of the web page to fetch.

        Returns:
            BeautifulSoup: A parsed HTML document.

        Raises:
            SystemExit: If all retry attempts fail, logs the error and exits the program.
        """

        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers, timeout=5)
                response.raise_for_status()

                return BeautifulSoup(response.content, "html.parser")
            except requests.exceptions.RequestException as e:
                logger.error(f"Attempt {attempt} failed to fetch page {url}: {e}")

                if attempt < self.MAX_RETRIES:
                    logger.info(f"Retrying in {self.RETRY_DELAY} seconds...")
                    time.sleep(self.RETRY_DELAY)
                else:
                    logger.error(f"All {self.MAX_RETRIES} attempts failed for {url}. Exiting.")
                    sys.exit(1)

        # This should never be reached, but I have added it for safety.
        raise RuntimeError("Unexpected code path reached in fetch method")
