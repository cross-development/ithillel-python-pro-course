"""
Asynchronous Image Downloader with Aiohttp.
This script downloads multiple images in parallel using aiohttp and asyncio.
"""

import os
import asyncio
from typing import List, Tuple

import aiohttp


async def download_image(url: str, filename: str) -> None:
    """
    Downloads an image from a given URL and saves it to the specified filename.

    Args:
        url (str): The URL of the image to download.
        filename (str): The local file path where the image will be saved.

    Returns:
        None
    """

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    # Ensure the directory exists
                    os.makedirs(os.path.dirname(filename), exist_ok=True)

                    with open(filename, "wb") as f:
                        f.write(await response.read())

                    print(f"Downloaded: {filename}")
                else:
                    print(f"Failed to download {url}: HTTP {response.status}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


async def main() -> None:
    """
    Main function that initializes and runs multiple asynchronous download tasks.

    Returns:
        None
    """

    test_urls: List[Tuple[str, str]] = [
        ("https://i.ytimg.com/vi/dTSgbztJ7Io/maxresdefault.jpg", "images/image_1.jpg"),
        ("https://i.ytimg.com/vi/5sBj-6BUOZA/maxresdefault.jpg", "images/image_2.jpg"),
        ("https://i.ytimg.com/vi/x_9SdeVjfe4/maxresdefault.jpg", "images/image_3.jpg"),
    ]
    tasks = [download_image(url, filename) for url, filename in test_urls]

    await asyncio.gather(*tasks)

    print("\nAll downloads completed.")


if __name__ == "__main__":
    print("Starting asynchronous image downloads...")
    asyncio.run(main())
