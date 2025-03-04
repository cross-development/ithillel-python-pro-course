"""
Asynchronous Web Page Downloader.
This script simulates downloading multiple web pages concurrently using asyncio.
"""

import random
import asyncio
from typing import List

from hw_13.utils import validate_urls
from hw_13.logger_config import logging
from hw_13.request_config import CONCURRENT_DOWNLOAD_LIMIT

logger = logging.getLogger(__name__)

# Semaphore to limit the number of concurrent downloads
semaphore = asyncio.Semaphore(CONCURRENT_DOWNLOAD_LIMIT)


async def download_page(url: str) -> None:
    """
    Simulates downloading a web page with a random delay.

    Args:
        url (str): The URL of the web page to download.

    Returns:
        None
    """

    async with semaphore:
        sleep_time = random.randint(1, 5)
        await asyncio.sleep(sleep_time)

        logger.info(f"Page {url} has been downloaded in {sleep_time} seconds.")


async def main(urls: List[str]) -> None:
    """
    Asynchronously downloads multiple web pages.

    Args:
        urls (List[str]): A list of URLs to download.

    Returns:
        None
    """

    valid_urls = validate_urls(urls)

    if not valid_urls:
        logger.error("No valid URLs were provided.")
        return

    tasks = [download_page(url) for url in valid_urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    test_urls: List[str] = [
        "https://example.com",
        "https://test.com",
        "https://google.com",
        "https://facebook.com",
        "https://github.com"
    ]

    logger.info("Starting downloads...")
    asyncio.run(main(test_urls))
    logger.info("All downloads completed!")
