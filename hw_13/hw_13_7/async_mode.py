"""
Asynchronous HTTP Requests with Aiohttp.
This script sends multiple asynchronous requests to given URLs and measures execution time.
"""

import asyncio
from typing import List

import aiohttp


async def async_request(session: aiohttp.ClientSession, url: str) -> int:
    """
    Sends an asynchronous GET request to the specified URL.

    Args:
        session (aiohttp.ClientSession): The active session for making requests.
        url (str): The target URL.

    Returns:
        int: The HTTP status code of the response.
    """

    async with session.get(url) as response:
        return response.status


async def main(urls: List[str]) -> None:
    """
    Main function that asynchronously sends multiple HTTP requests.

    Args:
        urls (List[str]): A list of URLs to request.

    Returns:
        None
    """

    start_time = asyncio.get_event_loop().time()
    print("Starting async requests...")

    async with aiohttp.ClientSession() as session:
        tasks = [async_request(session, url) for url in urls]
        await asyncio.gather(*tasks)

    elapsed_time = asyncio.get_event_loop().time() - start_time
    print(f"Total time (async): {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    test_urls = ["https://jsonplaceholder.typicode.com/todos/"] * 500
    asyncio.run(main(test_urls))
