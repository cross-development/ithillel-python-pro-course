"""
Multi-threaded File Downloader.

This module allows downloading multiple files concurrently using threading.
"""

import threading
import requests
from typing import List, Tuple


def download_file(url: str, filename: str) -> None:
    """
    Downloads a file from a given URL and saves it locally.

    Args:
        url (str): The URL of the file to download.
        filename (str): The local filename to save the downloaded content.

    Raises:
        requests.RequestException: If the request fails.
    """

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded {filename} from {url}")
    except requests.RequestException as e:
        print(f"Failed to download {filename} from {url}: {e}")


def download_files_concurrently(urls: List[Tuple[str, str]]) -> None:
    """
    Downloads multiple files concurrently using threading.

    Args:
        urls (List[Tuple[str, str]]): A list of tuples containing (URL, filename).
    """

    threads = []

    for url, filename in urls:
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All files downloaded.")


if __name__ == "__main__":
    urls_to_download = [
        ("https://i.ytimg.com/vi/dTSgbztJ7Io/maxresdefault.jpg", "images/image_1.jpg"),
        ("https://i.ytimg.com/vi/5sBj-6BUOZA/maxresdefault.jpg", "images/image_2.jpg"),
        ("https://i.ytimg.com/vi/x_9SdeVjfe4/maxresdefault.jpg", "images/image_3.jpg"),
    ]

    download_files_concurrently(urls_to_download)
