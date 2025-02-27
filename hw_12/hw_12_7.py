"""
Parallel Computation of Factorials Using Multiprocessing.
This script calculates the factorial of large numbers in parallel.
"""

import sys
import multiprocessing
from multiprocessing import managers
from math import factorial

# Increase the limit for converting integers to strings (allow up to 100 million digits)
sys.set_int_max_str_digits(10 ** 8)


def compute_factorial(number: int, result: managers.ListProxy, index: int) -> None:
    """
    Computes the factorial of a given number and stores the result.

    Args:
        number (int): The number to compute the factorial for.
        result (managers.ListProxy): A shared list to store results.
        index (int): The index in the results list for storing the computed factorial.
    """

    result[index] = factorial(number)


def main() -> None:
    """
    Main function to compute factorials in parallel.
    """

    numbers = [100000, 200000, 300000]

    with multiprocessing.Manager() as manager:
        result = manager.list([0] * len(numbers))
        processes = []

        for i, number in enumerate(numbers):
            process = multiprocessing.Process(target=compute_factorial, args=(number, result, i))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print("\nFactorials computed:")

        for num, fact in zip(numbers, result):
            fact_str = str(fact)
            digits = len(fact_str)
            print(f"{num}! = {fact_str[:60]}... ({digits} digits total)")


if __name__ == "__main__":
    main()
