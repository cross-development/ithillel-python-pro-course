from typing import List

from hw_5.hw_5_2.processors.file_processor import FileProcessor


class AverageCalculator(FileProcessor):
    """
    A FileProcessor that calculates the average of numbers in a file.
    """

    def _extract_numbers(self, lines: List[str]) -> List[float]:
        """
        Extracts floating-point numbers from the lines of the file.

        Args:
            lines (List[str]): A list of strings, where each string is a line from the file.

        Raises:
            ValueError: If a line cannot be converted to a float.

        Returns:
            List[float]: A list of floating-point numbers.
        """
        numbers = []

        for line in lines:
            line = line.strip()

            if line:
                try:
                    numbers.append(float(line))
                except ValueError:
                    raise ValueError(f"Invalid data in file: '{line}' is not a number.")

        return numbers

    def _calculate(self, numbers: List[float]) -> float:
        """
        Calculates the average of the numbers.

        Args:
            numbers (List[float]): A list of floating-point numbers.

        Raises:
            ZeroDivisionError: If the list of numbers is empty.

        Returns:
            float: The average of the numbers.
        """
        if not numbers:
            raise ZeroDivisionError

        return sum(numbers) / len(numbers)
