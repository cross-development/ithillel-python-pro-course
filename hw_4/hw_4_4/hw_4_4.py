from typing import Generator


def filter_log_file(input_file: str, output_file: str, keyword: str) -> None:
    """
    Reads a large file line by line and filters lines containing a keyword.
    Writes the filtered lines to a new output file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
        keyword (str): Keyword to filter lines by.
    """

    def line_generator() -> Generator[str, None, None]:
        """
        Generates lines from the input file that contain the keyword.

        Yields:
            str: The next line containing the keyword.
        """
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                if keyword.lower() in line.lower():
                    yield line

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filtered_line in line_generator():
            outfile.write(filtered_line)


filter_log_file(
    input_file='large_log.txt',
    output_file='error_logs.txt',
    keyword='error'
)

print("All tests passed!")
