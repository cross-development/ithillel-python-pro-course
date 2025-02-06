"""
This module contains unit tests for the FileProcessor class.

- `test_file_write_read`: Tests writing and reading data to/from a file.
- `test_empty_file`: Tests writing and reading an empty file.
- `test_large_data`: Tests writing and reading a large amount of data.
- `test_file_not_found`: Tests the FileNotFoundError handling for reading a non-existent file.
"""

import pytest

from hw_7.hw_7_7.file_processor import FileProcessor


def test_file_write_read(tmpdir: str) -> None:
    """
    Tests writing and reading data to/from a file.

    Args:
        tmpdir (str): A temporary directory fixture provided by pytest.
    """

    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)

    assert content == "Hello, World!"


def test_empty_file(tmpdir: str) -> None:
    """
    Tests writing and reading an empty file.

    Args:
        tmpdir (str): A temporary directory fixture provided by pytest.
    """

    file = tmpdir.join("empty.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)

    assert content == ""


def test_large_data(tmpdir: str) -> None:
    """
    Tests writing and reading a large amount of data.

    Args:
        tmpdir (str): A temporary directory fixture provided by pytest.
    """

    file = tmpdir.join("large.txt")
    large_text = "A" * 10 ** 6
    FileProcessor.write_to_file(file, large_text)
    content = FileProcessor.read_from_file(file)

    assert content == large_text


def test_file_not_found() -> None:
    """
    Tests the FileNotFoundError handling for reading a non-existent file.
    """

    with pytest.raises(FileNotFoundError, match="File non_existing.txt not found"):
        FileProcessor.read_from_file("non_existing.txt")


if __name__ == "__main__":
    pytest.main()
