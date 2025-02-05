"""
This module provides a simple entry point for the AverageCalculator.

It creates an instance of the AverageCalculator, processes the specified file,
and displays the calculated average if successful.
"""

from hw_5.hw_5_2.processors.average_calculator import AverageCalculator

if __name__ == '__main__':
    FILENAME = "data/numbers.txt"
    calculator = AverageCalculator(FILENAME)
    result = calculator.process()

    if result is not None:
        print(f"Average: {result}")
