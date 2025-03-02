"""
Multithreading HTTP Requests.
This script sends multiple HTTP requests concurrently using threading and measures execution time.
"""

import time
import threading
from typing import List

import requests


def thread_request(url: str) -> int:
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
    Main function that processes multiple HTTP requests using threading.

    Args:
        urls (List[str]): A list of URLs to request.

    Returns:
        None
    """

    start_time = time.time()
    print("Starting multithreading requests...")

    threads = [threading.Thread(target=thread_request, args=(url,)) for url in urls]

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    elapsed_time = time.time() - start_time
    print(f"Total time (multithreading): {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    test_urls = ["https://jsonplaceholder.typicode.com/todos/"] * 500
    main(test_urls)
