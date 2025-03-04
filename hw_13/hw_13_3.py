"""
Asynchronous Producer-Consumer Queue.
This script demonstrates an asynchronous producer-consumer pattern using asyncio.
"""

import asyncio

from hw_13.logger_config import logging

logger = logging.getLogger(__name__)


async def producer(queue: asyncio.Queue) -> None:
    """
    Produces tasks and puts them into the queue.

    Args:
        queue (asyncio.Queue): The queue where tasks will be placed.

    Returns:
        None
    """

    number_of_tasks = 5

    for i in range(number_of_tasks):
        await asyncio.sleep(1)

        task = f"Task {i + 1}"
        await queue.put(task)

        logging.info(f"Producer added {task}")


async def consumer(queue: asyncio.Queue, consumer_id: int) -> None:
    """
    Consumes tasks from the queue and processes them.

    Args:
        queue (asyncio.Queue): The queue to retrieve tasks from.
        consumer_id (int): The identifier for the consumer.

    Returns:
        None
    """

    while True:
        task = await queue.get()

        if task is None:
            break

        logging.info(f"Consumer {consumer_id} started {task}")
        await asyncio.sleep(2)
        logging.info(f"Consumer {consumer_id} completed {task}")

        queue.task_done()


async def main() -> None:
    """
    Main function to manage producer and consumer coroutines.

    Returns:
        None
    """

    number_of_consumers = 2
    queue = asyncio.Queue()

    # Create consumers
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(number_of_consumers)]

    # Start producer
    await producer(queue)

    # Wait for all tasks to be processed
    await queue.join()

    # Stop consumers
    for _ in consumers:
        await queue.put(None)

    await asyncio.gather(*consumers)


if __name__ == "__main__":
    logging.info("Starting Producer-Consumer Process...")
    asyncio.run(main())
    logging.info("All tasks completed!")
