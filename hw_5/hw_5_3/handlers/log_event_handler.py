"""
This module provides a simple logging function for game events.

The `log_event` function takes a GameEventException object
as input and prints a log message containing the event type
and its associated details.
"""

from hw_5.hw_5_3.exceptions.game_event_exception import GameEventException


def log_event(event: GameEventException) -> None:
    """
    Logs a game event.

    Args:
        event (GameEventException): The game event to log.
    """
    print(f"[LOG] {event.event_type}: {event.details}")
