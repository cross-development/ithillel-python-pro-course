from hw_5.hw_5_3.event_types import EventType
from hw_5.hw_5_3.exceptions.game_event_exception import GameEventException


def show_user_message(event: GameEventException) -> None:
    """
    Displays a user-friendly message for a game event.

    Args:
        event (GameEventException): The game event to display a message for.
    """
    match event.event_type:
        case EventType.DEATH:
            print(f"💀 You died! Cause: {event.details.get('cause', 'Unknown')}")
        case EventType.LEVEL_UP:
            print(f"🎉 Level up! New level: {event.details.get('new_level')}")
        case _:
            print("Unknown event type")
