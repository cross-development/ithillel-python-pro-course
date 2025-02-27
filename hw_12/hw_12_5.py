"""
Multithreaded File Search.

This script searches for a keyword in multiple files concurrently using threads.
"""

import threading
from typing import List


def search_in_file(filename: str, keyword: str) -> None:
    """
    Searches for a keyword in a given file and prints matching lines.

    Args:
        filename (str): The file to search in.
        keyword (str): The keyword to search for.
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                position = line.find(keyword)

                while position != -1:
                    print(f"Found '{keyword}' in {filename} at line {line_number}:{position + 1}")
                    position = line.find(keyword, position + 1)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")


def search_in_files(filenames: List[str], keyword: str) -> None:
    """
    Searches for a keyword in multiple files using threads.

    Args:
        filenames (List[str]): List of filenames to search in.
        keyword (str): The keyword to search for.
    """

    threads = []

    for filename in filenames:
        thread = threading.Thread(target=search_in_file, args=(filename, keyword))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Search completed.")


if __name__ == "__main__":
    SEARCH_TERM = "Python"
    files_to_search = ["text/file_1.txt", "text/file_2.txt", "text/file_3.txt"]

    search_in_files(files_to_search, SEARCH_TERM)
