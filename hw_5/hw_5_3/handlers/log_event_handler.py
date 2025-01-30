from hw_5.hw_5_3.exceptions.game_event_exception import GameEventException


def log_event(event: GameEventException) -> None:
    """
    Logs a game event.

    Args:
        event (GameEventException): The game event to log.
    """
    print(f"[LOG] {event.event_type}: {event.details}")
