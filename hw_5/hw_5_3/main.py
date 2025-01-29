from event_dispatcher import EventDispatcher
from hw_5.hw_5_3.event_types import EventType
from exceptions.game_event_exception import GameEventException
from hw_5.hw_5_3.handlers.log_event_handler import log_event
from hw_5.hw_5_3.handlers.show_user_message_handler import show_user_message


def simulate_game_events(dispatcher: EventDispatcher) -> None:
    """
    Simulates game events and dispatches them using the event dispatcher.

    Args:
        dispatcher (EventDispatcher): The event dispatcher to use.
    """
    try:
        raise GameEventException(EventType.DEATH, {"cause": "sword attack", "damage": "15"})
    except GameEventException as e:
        dispatcher.dispatch(e)

    try:
        raise GameEventException(EventType.LEVEL_UP, {"new_level": 5, "xp_gained": 150})
    except GameEventException as e:
        dispatcher.dispatch(e)


if __name__ == '__main__':
    event_dispatcher = EventDispatcher()

    event_dispatcher.subscribe(EventType.DEATH, log_event)
    event_dispatcher.subscribe(EventType.DEATH, show_user_message)

    event_dispatcher.subscribe(EventType.LEVEL_UP, log_event)
    event_dispatcher.subscribe(EventType.LEVEL_UP, show_user_message)

    simulate_game_events(event_dispatcher)
