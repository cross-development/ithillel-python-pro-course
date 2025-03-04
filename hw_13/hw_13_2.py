"""
Asynchronous Web Page Fetcher.
This script fetches the content of multiple web pages concurrently using aiohttp and asyncio.
"""

import asyncio
from typing import List

import aiohttp

from hw_13.utils import validate_urls
from hw_13.logger_config import logging
from hw_13.request_config import SHORT_REQUEST_TIMEOUT, CONCURRENT_REQUEST_LIMIT

logger = logging.getLogger(__name__)

# Semaphore to limit the number of concurrent requests
semaphore = asyncio.Semaphore(CONCURRENT_REQUEST_LIMIT)


async def fetch_content(session: aiohttp.ClientSession, url: str) -> str:
    """
    Asynchronously fetches the content of a web page.

    Args:
        session (aiohttp.ClientSession): The active session for making requests.
        url (str): The URL to fetch.

    Returns:
        str: The content of the web page if successful, or an error message otherwise.
    """

    async with semaphore:
        try:
            async with session.get(url, timeout=SHORT_REQUEST_TIMEOUT) as response:
                if response.status == 200:
                    return await response.text()

                return f"Error: status {response.status}"
        except aiohttp.ClientError as e:
            logger.error(f"Client error occurred while requesting {url}: {e}")
        except asyncio.TimeoutError:
            logger.error(f"Request to {url} timed out")
        except Exception as e:
            logger.error(f"Unexpected error occurred while requesting {url}: {e}")


async def fetch_all(urls: List[str]) -> None:
    """
    Asynchronously fetches multiple web pages and prints a summary of their content.

    Args:
        urls (List[str]): A list of URLs to fetch.

    Returns:
        None
    """

    valid_urls = validate_urls(urls)

    if not valid_urls:
        logger.error("No valid URLs were provided.")
        return

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_content(session, url) for url in valid_urls]
        results = await asyncio.gather(*tasks)

    logger.info("Fetch results:")

    for url, content in zip(valid_urls, results):
        # Truncate output for readability (just for testing purpose)
        logger.info(f"{url} → {content[:60]}...")


if __name__ == "__main__":
    test_urls: List[str] = [
        "https://nonexistent.url",
        "https://www.google.com/",
        "https://news.ycombinator.com/ ",
        "https://www.reddit.com/",
    ]

    logger.info("Starting fetch process...")
    asyncio.run(fetch_all(test_urls))
    logger.info("Fetching completed!")
