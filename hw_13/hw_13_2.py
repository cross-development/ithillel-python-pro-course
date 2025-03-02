"""
Asynchronous Web Page Fetcher.
This script fetches the content of multiple web pages concurrently using aiohttp and asyncio.
"""

import asyncio
from typing import List

import aiohttp


async def fetch_content(url: str) -> str:
    """
    Asynchronously fetches the content of a web page.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the web page if successful, or an error message otherwise.
    """

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()

                return f"Error: status {response.status}"
    except aiohttp.ClientConnectionError:
        return f"Error: cannot connect to {url}"
    except Exception as e:
        return f"Error: unexpected error {e}"


async def fetch_all(urls: List[str]) -> None:
    """
    Asynchronously fetches multiple web pages and prints a summary of their content.

    Args:
        urls (List[str]): A list of URLs to fetch.

    Returns:
        None
    """

    tasks = [fetch_content(url) for url in urls]
    results = await asyncio.gather(*tasks)

    print("\nFetch results:")

    for url, content in zip(urls, results):
        print(f"{url} → {content[:60]}...")  # Truncate output for readability


if __name__ == "__main__":
    test_urls = [
        "https://nonexistent.url",
        "https://news.ycombinator.com/",
        "https://www.google.com/",
    ]

    print("Starting fetch process...\n")
    asyncio.run(fetch_all(test_urls))
    print("\nFetching completed!")
