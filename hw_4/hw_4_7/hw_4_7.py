import re
from typing import Iterator


def error_line_generator(log_file_path: str) -> Iterator[str]:
    """
    Generates lines containing error codes (4XX or 5XX) from a log file.

    Args:
        log_file_path (str): Path to the log file.

    Yields:
        str: The next line containing an error code.

    Raises:
        FileNotFoundError: If the log file is not found.
    """
    error_pattern = re.compile(r'\s(4\d{2}|5\d{2})\s')

    try:
        with open(log_file_path, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if error_pattern.search(line):
                    yield line
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file '{log_file_path}' not found.")


def extract_errors_to_file(log_file_path: str, output_file_path: str) -> None:
    """
    Extracts error lines from a log file and writes them to a new file.

    Args:
        log_file_path (str): Path to the log file.
        output_file_path (str): Path to the output file where errors will be written.

    Raises:
        FileNotFoundError: If the log file or output file cannot be opened.
        Exception: For any other unexpected errors.
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for error_line in error_line_generator(log_file_path):
                output_file.write(error_line)

        print(f"Error lines have been written to '{output_file_path}'.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


log_file_pathname = "server.log"
output_file_pathname = "errors.log"

extract_errors_to_file(log_file_pathname, output_file_pathname)

print("All tests passed!")
