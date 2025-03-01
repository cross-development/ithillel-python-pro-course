"""
Parallel Computation of Factorials Using Multiprocessing.
This script calculates the factorial of large numbers in parallel using math.factorial.
"""

import sys
from multiprocessing import Pool, cpu_count
from math import factorial
from time import perf_counter
from typing import Tuple

# Increase the limit for converting integers to strings (allow up to 100 million digits)
# This is necessary because very large factorials can exceed the default string conversion limit.
sys.set_int_max_str_digits(10 ** 8)


def compute_factorial(number: int) -> Tuple[int, str, float]:
    """
    Computes the factorial of a given number.

    Args:
        number (int): The number to compute the factorial for.

    Returns:
        Tuple[int, str, float]: A tuple containing:
            - The original number.
            - The computed factorial as a string.
            - The time taken to compute the factorial.
    """

    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    start_time = perf_counter()

    try:
        result = factorial(number)
    except OverflowError:
        return number, "OverflowError: Result too large to compute.", perf_counter() - start_time

    elapsed_time = perf_counter() - start_time

    return number, str(result), elapsed_time


def main() -> None:
    """
    Main function to compute factorials in parallel using multiprocessing.Pool.
    """

    # Input numbers for which we want to compute factorials
    numbers = [100000, 200000, 300000]

    # Configure output options
    max_output_length = 60  # Maximum number of characters to display for each factorial
    use_exponential_format = False  # Whether to use exponential format for very large numbers

    print("Starting parallel factorial computation...\n")

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(compute_factorial, numbers)

    for number, fact, elapsed_time in results:
        if isinstance(fact, str) and fact.startswith("OverflowError"):
            print(f"{number}! = {fact}")
        else:
            digits = len(fact)
            formatted_fact = f"{fact[:max_output_length]}..." \
                if len(fact) > max_output_length else fact

            if use_exponential_format and digits > max_output_length:
                formatted_fact = f"{fact[0]}.{fact[1:max_output_length - 5]}e+{digits - 1}"

            print(f"{number}! = {formatted_fact} ({digits} digits total)")

        print(f"Time taken: {elapsed_time:.4f} seconds\n")


if __name__ == "__main__":
    main()
