"""Background task to log meeting creation."""

import time


def log_new_meeting(topic: str) -> None:
    time.sleep(2)

    print(f"[BackgroundTask] New meeting created with topic: {topic}")
