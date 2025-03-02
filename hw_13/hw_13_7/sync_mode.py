"""
Synchronous HTTP Requests.
This script sends multiple HTTP requests sequentially and measures execution time.
"""

import time
from typing import List

import requests


def sync_request(url: str) -> int:
    """
    Sends a synchronous GET request to the specified URL and returns the status code.

    Args:
        url (str): The target URL.

    Returns:
        int: The HTTP status code of the response.
    """

    try:
        response = requests.get(url, timeout=5)

        return response.status_code
    except requests.RequestException as e:
        print(f"Error: Failed to fetch {url} - {e}")
        return 0


def main(urls: List[str]) -> None:
    """
    Main function that processes multiple HTTP requests sequentially.

    Args:
        urls (List[str]): A list of URLs to request.

    Returns:
        None
    """

    start_time = time.time()
    print("Starting synchronous requests...")

    for url in urls:
        sync_request(url)

    elapsed_time = time.time() - start_time
    print(f"Total time (sync): {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    test_urls = ["https://jsonplaceholder.typicode.com/todos/"] * 500
    main(test_urls)
