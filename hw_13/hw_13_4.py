"""
Asynchronous Task with Timeout Handling.
This script demonstrates how to use asyncio.wait_for() to set a timeout for an asynchronous task.
"""

import asyncio


async def slow_task() -> None:
    """
    Simulates a slow asynchronous task by sleeping for 10 seconds.

    Returns:
        None
    """

    await asyncio.sleep(10)
    print("Task finished")


async def main() -> None:
    """
    Runs the slow task with a timeout limit.
    If the task exceeds the given timeout, an asyncio.TimeoutError is raised.

    Returns:
        None
    """

    try:
        print("Starting slow task with a 5-second timeout...")

        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("The waiting time has been exceeded!")


if __name__ == "__main__":
    print("Running the async timeout example...\n")
    asyncio.run(main())
    print("\nProgram completed!")
