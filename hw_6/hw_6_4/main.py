"""
This module provides functions for managing a library of books stored in a JSON file.

**Key functionalities:**

- **load_books():** Loads a list of books from the 'books.json' file.
- **save_books(books):** Saves a list of books to the 'books.json' file.
- **list_available_books():** Prints a list of currently available books.
- **add_book(name, author, year, available):** Adds a new book to the library.

The script demonstrates the usage of these functions by:

1. Listing the initially available books.
2. Prompting the user to enter details for a new book.
3. Adding the new book to the library.
4. Listing the available books after the addition.
"""

import json
from typing import List, Dict

FILENAME = "books.json"


def load_books() -> List[Dict]:
    """
    Loads a list of books from a JSON file.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary represents a book with keys
                   'name', 'author', 'year', and 'available'.
    """

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books: List[Dict]) -> None:
    """
    Saves a list of books to a JSON file.

    Args:
        books (List[Dict]): A list of dictionaries, where each dictionary represents a book.
    """

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)


def list_available_books() -> None:
    """
    Prints a list of available books from the JSON file.
    """

    books = load_books()

    available_books = [book for book in books if book.get("available", False)]

    if available_books:
        print("Available books:")

        for book in available_books:
            print(f'  - "{book["name"]}" by {book["author"]} ({book["year"]})')
    else:
        print("No available books.")


def add_book(name: str, author: str, year: int, available: bool) -> None:
    """
    Adds a new book to the list of books in the JSON file.

    Args:
        name (str): The name of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
        available (bool): Whether the book is currently available.
    """

    books = load_books()
    books.append({
        "name": name,
        "author": author,
        "year": year,
        "available": available,
    })

    save_books(books)
    print(f"Book '{name}' has been added!")


if __name__ == "__main__":
    list_available_books()

    new_name = input("Enter book name: ")
    new_author = input("Author: ")
    new_year = int(input("Year: "))
    new_available = input("Is available? (yes/no): ").strip().lower() == "yes"

    add_book(new_name, new_author, new_year, new_available)

    list_available_books()
