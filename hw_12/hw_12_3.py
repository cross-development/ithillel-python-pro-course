"""
Parallel Sum Calculation.

This module calculates the sum of a large list using multiprocessing.
"""

from multiprocessing import managers, Manager, Process
from typing import List


def sum_part(numbers: List[int], result: managers.ListProxy, index: int) -> None:
    """
    Computes the sum of a part of the list and stores it in a shared list.

    Args:
        numbers (List[int]): Sublist of numbers to sum.
        result (managers.ListProxy): Shared list to store results.
        index (int): Index position in the shared list.
    """

    result[index] = sum(numbers)


def parallel_sum(numbers: List[int], num_processes: int = 4) -> int:
    """
    Splits a list into chunks and calculates their sum in parallel.

    Args:
        numbers (List[int]): List of numbers to sum.
        num_processes (int, optional): Number of processes to use. Defaults to 4.

    Returns:
        int: Total sum of the list.
    """

    chunk_size = len(numbers) // num_processes

    with Manager() as manager:
        result = manager.list([0] * num_processes)
        processes = []

        for i in range(num_processes):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i != num_processes - 1 else len(numbers)
            process = Process(target=sum_part, args=(numbers[start:end], result, i))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return sum(result)


if __name__ == "__main__":
    numbers_to_sum = list(range(1_000_000))
    total = parallel_sum(numbers_to_sum)

    print(f"Total sum: {total}")
