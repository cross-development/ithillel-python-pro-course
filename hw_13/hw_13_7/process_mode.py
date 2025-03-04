"""
Parallel HTTP Requests Using Multiprocessing.
This script sends multiple HTTP requests in parallel using multiprocessing
and measures execution time.
"""

import time
from typing import List
from multiprocessing import Pool

import requests

from hw_13.utils import validate_urls
from hw_13.logger_config import logging
from hw_13.request_config import NUMBER_OF_REQUESTS, LONG_REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


def process_request(url: str) -> int:
    """
    Sends a synchronous GET request to the specified URL and returns the status code.

    Args:
        url (str): The target URL.

    Returns:
        int: The HTTP status code of the response, or -1 if an error occurs.
    """

    try:
        logger.info(f"Sending request to {url}")

        response = requests.get(url, timeout=LONG_REQUEST_TIMEOUT)
        return response.status_code
    except requests.Timeout:
        logger.error(f"Request to {url} timed out")
    except requests.ConnectionError:
        logger.error(f"Connection error occurred while requesting {url}")
    except requests.RequestException as e:
        logger.error(f"Request error occurred while requesting {url}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred while requesting {url}: {e}")

    # Return -1 to indicate an error
    return -1


def main(urls: List[str]) -> None:
    """
    Main function that processes multiple HTTP requests in parallel.

    Args:
        urls (List[str]): A list of URLs to request.

    Returns:
        None
    """

    valid_urls = validate_urls(urls)
    mult_valid_urls = valid_urls * NUMBER_OF_REQUESTS

    start_time = time.time()
    logger.info("Starting parallel requests...")

    with Pool() as pool:
        pool.map(process_request, mult_valid_urls)

    elapsed_time = time.time() - start_time
    logger.info(f"Total time (multiprocessing): {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    test_urls = ["https://jsonplaceholder.typicode.com/todos/"]
    main(test_urls)
