"""
Asynchronous HTTP Requests with Aiohttp.
This script sends multiple asynchronous requests to given URLs and measures execution time.
"""

import asyncio
from typing import List

import aiohttp

from hw_13.utils import validate_urls
from hw_13.logger_config import logging
from hw_13.request_config import NUMBER_OF_REQUESTS, LONG_REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


async def async_request(session: aiohttp.ClientSession, url: str) -> int:
    """
    Sends an asynchronous GET request to the specified URL.

    Args:
        session (aiohttp.ClientSession): The active session for making requests.
        url (str): The target URL.

    Returns:
        int: The HTTP status code of the response, or -1 if an error occurs.
    """

    try:
        logger.info(f"Sending request to {url}")

        async with session.get(url, timeout=LONG_REQUEST_TIMEOUT) as response:
            return response.status
    except aiohttp.ClientError as e:
        logger.error(f"Client error occurred while requesting {url}: {e}")
    except asyncio.TimeoutError:
        logger.error(f"Request to {url} timed out")
    except Exception as e:
        logger.error(f"Unexpected error occurred while requesting {url}: {e}")

    # Return -1 to indicate an error
    return -1


async def main(urls: List[str]) -> None:
    """
    Main function that asynchronously sends multiple HTTP requests.

    Args:
        urls (List[str]): A list of URLs to request.

    Returns:
        None
    """

    valid_urls = validate_urls(urls)
    mult_valid_urls = valid_urls * NUMBER_OF_REQUESTS

    start_time = asyncio.get_event_loop().time()
    logger.info("Starting async requests...")

    async with aiohttp.ClientSession() as session:
        tasks = [async_request(session, url) for url in mult_valid_urls]
        await asyncio.gather(*tasks)

    elapsed_time = asyncio.get_event_loop().time() - start_time
    logger.info(f"Total time (async): {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    test_urls = ["https://jsonplaceholder.typicode.com/todos/"]
    asyncio.run(main(test_urls))
