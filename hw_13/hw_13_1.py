"""
Asynchronous Web Page Downloader.
This script simulates downloading multiple web pages concurrently using asyncio.
"""

import random
import asyncio
from typing import List


async def download_page(url: str) -> None:
    """
    Simulates downloading a web page with a random delay.

    Args:
        url (str): The URL of the web page to download.

    Returns:
        None
    """

    sleep_time = random.randint(1, 5)
    await asyncio.sleep(sleep_time)

    print(f"Page {url} has been downloaded in {sleep_time} seconds.")


async def main(urls: List[str]) -> None:
    """
    Asynchronously downloads multiple web pages.

    Args:
        urls (List[str]): A list of URLs to download.

    Returns:
        None
    """

    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    test_urls = ["https://example.com", "https://test.com", "https://google.com"]

    print("Starting downloads...\n")
    asyncio.run(main(test_urls))
    print("\nAll downloads completed!")
