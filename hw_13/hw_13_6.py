"""
Asynchronous Image Downloader with Aiohttp.
This script downloads multiple images in parallel using aiohttp and asyncio.
"""

import os
import asyncio
from typing import List, Tuple

import aiohttp

from hw_13.utils import validate_urls
from hw_13.logger_config import logging
from hw_13.request_config import LONG_REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


async def download_image(session: aiohttp.ClientSession, url: str, filename: str) -> None:
    """
    Downloads an image from a given URL and saves it to the specified filename.

    Args:
        session (aiohttp.ClientSession): The active session for making requests.
        url (str): The URL of the image to download.
        filename (str): The local file path where the image will be saved.

    Returns:
        None
    """

    try:
        async with session.get(url, timeout=LONG_REQUEST_TIMEOUT) as response:
            if response.status == 200:
                # Ensure the directory exists
                os.makedirs(os.path.dirname(filename), exist_ok=True)

                with open(filename, "wb") as f:
                    f.write(await response.read())

                logger.info(f"Downloaded: {filename}")
            else:
                logger.error(f"Failed to download {url}: HTTP {response.status}")
    except aiohttp.ClientError as e:
        logger.error(f"Client error occurred while requesting {url}: {e}")
    except asyncio.TimeoutError:
        logger.error(f"Request to {url} timed out")
    except Exception as e:
        logger.error(f"Unexpected error occurred while requesting {url}: {e}")


async def main(urls: List[Tuple[str, str]]) -> None:
    """
    Main function that initializes and runs multiple asynchronous download tasks.

    Args:
        urls (List[Tuple[str, str]]): A list of URLs to download.

    Returns:
        None
    """

    valid_urls = validate_urls(urls)

    if not valid_urls:
        logger.error("No valid URLs were provided.")
        return

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, filename) for url, filename in valid_urls]
        await asyncio.gather(*tasks)

    logger.info("All downloads completed.")


if __name__ == "__main__":
    test_urls: List[Tuple[str, str]] = [
        ("https://i.ytimg.com/vi/dTSgbztJ7Io/maxresdefault.jpg", "images/image_1.jpg"),
        ("https://i.ytimg.com/vi/5sBj-6BUOZA/maxresdefault.jpg", "images/image_2.jpg"),
        ("https://i.ytimg.com/vi/x_9SdeVjfe4/maxresdefault.jpg", "images/image_3.jpg"),
    ]

    logger.info("Starting asynchronous image downloads...")
    asyncio.run(main(test_urls))
