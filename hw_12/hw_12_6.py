"""
Multi-processing Simulation of Organism Survival with Iterations.

This script simulates the survival of organisms over multiple iterations using multiprocessing.
"""

import random
import multiprocessing
from multiprocessing import managers
from typing import List


class Organism:
    """
    Represents an organism with a limited amount of food.
    """

    def __init__(self, food: int = 100) -> None:
        """
        Initializes an organism with a given amount of food.

        Args:
            food (int): The initial food supply. Defaults to 100.
        """

        self.food = food

    def survive(self) -> bool:
        """
        Simulates a survival attempt by reducing food.

        Returns:
            bool: True if the organism survives, False otherwise.
        """

        self.food -= random.randint(5, 15)

        return self.food > 0


def simulate_population(population: List[Organism],
                        results: managers.ListProxy, index: int) -> None:
    """
    Simulates the survival of a population over multiple iterations.

    Args:
        population (List[Organism]): The group of organisms.
        results (managers.ListProxy): Shared list to store survival results.
        index (int): Index in the results list for this process.
    """

    survived = []

    for organism in population:
        # Simulate several iterations of survival
        for _ in range(5):  # Conduct 5 iterations for each organism
            if not organism.survive():
                break  # If the organism does not survive, stop iterating
        else:
            survived.append(organism)  # If it survived, add to the list

    results[index] = len(survived)


if __name__ == "__main__":
    NUM_ORGANISMS = 100
    NUM_GROUPS = 4
    GROUP_SIZE = NUM_ORGANISMS // NUM_GROUPS
    NUM_FOODS = random.randint(30, 100)  # Random food supply for each organism

    populations = [[Organism(NUM_FOODS) for _ in range(GROUP_SIZE)] for _ in range(NUM_GROUPS)]

    manager = multiprocessing.Manager()
    res = manager.list([0] * NUM_GROUPS)

    processes = []

    for i, p in enumerate(populations):
        process = multiprocessing.Process(target=simulate_population, args=(p, res, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_survived = sum(res)
    print(f"Total organisms survived: {total_survived}")
