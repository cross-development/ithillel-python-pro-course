"""
This module provides the PageDownloader class, a utility for downloading web pages.

The PageDownloader offers a static `download` method that:

- Fetches the content of a given URL using the `requests` library.
- Handles potential exceptions (e.g., network errors, timeout) gracefully.
- Returns the downloaded content as a string.
"""

import requests


class PageDownloader:
    """
    Utility class for downloading web pages.
    """

    @staticmethod
    def download(url: str) -> str:
        """
        Downloads a web page from the given URL.

        Args:
            url (str): The URL of the web page to download.

        Returns:
            str: The downloaded content of the web page, or an empty string on error.
        """

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            print(f"The {url} page has been successfully downloaded!")

            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")

            return ""
