"""
This module provides a WebService class for fetching data from web APIs.

- `get_data(url)`: Sends a GET request to the specified URL and returns the JSON response.
    Raises a `requests.RequestException` for network or HTTP errors.
"""

import requests


class WebService:
    """
    A class for interacting with web services.
    """

    def get_data(self, url: str) -> dict:
        """
        Retrieves JSON data from a given URL.

        Args:
            url (str): The URL to retrieve data from.

        Returns:
            dict: A dictionary containing the JSON response data.

        Raises:
            requests.RequestException: For network or HTTP errors.
        """

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
