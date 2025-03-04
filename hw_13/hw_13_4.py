"""
Asynchronous Task with Timeout Handling.
This script demonstrates how to use asyncio.wait_for() to set a timeout for an asynchronous task.
"""

import asyncio

from hw_13.logger_config import logging
from hw_13.request_config import SHORT_REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


async def slow_task() -> None:
    """
    Simulates a slow asynchronous task by sleeping for 10 seconds.

    Returns:
        None
    """

    try:
        logger.info("Slow task started.")
        await asyncio.sleep(10)
        logger.info("Slow task finished successfully.")
    except asyncio.CancelledError:
        logger.warning("Slow task was cancelled due to timeout!")
        raise  # Re-raise the CancelledError to propagate it


async def main() -> None:
    """
    Runs the slow task with a timeout limit.
    If the task exceeds the given timeout, an asyncio.TimeoutError is raised.
    Uses asyncio.shield() to allow the task to continue running in the background.

    Returns:
        None
    """

    logger.info("Starting slow task with a 5-second timeout...")

    task = asyncio.create_task(slow_task())

    try:
        # Using asyncio.wait_for with shield to protect the task from cancellation
        await asyncio.wait_for(asyncio.shield(task), timeout=SHORT_REQUEST_TIMEOUT)
    except asyncio.TimeoutError:
        logger.error("The waiting time has been exceeded! Task is still running in the background.")

        logger.info("Waiting for the background task to finish...")
        await task  # This ensures the task completes even after the timeout
    except Exception as e:
        logger.error(f"Error: unexpected error {e}")
    else:
        logger.info("Task completed within the timeout.")


if __name__ == "__main__":
    logging.info("Running the async timeout example...")
    asyncio.run(main())
    logging.info("Program completed!")
