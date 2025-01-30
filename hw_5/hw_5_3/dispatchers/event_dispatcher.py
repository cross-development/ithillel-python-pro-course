from typing import List, Callable, Dict

from hw_5.hw_5_3.enums.event_type import EventType
from hw_5.hw_5_3.exceptions.game_event_exception import GameEventException


class EventDispatcher:
    """
    Dispatches game events to registered handlers.

    Attributes:
        _subscribers (Dict[EventType, List[Callable[[GameEventException], None]]]):
            A dictionary mapping event types to lists of event handlers.
    """

    def __init__(self) -> None:
        """
        Initializes the EventDispatcher.
        """
        self._subscribers: Dict[EventType, List[Callable[[GameEventException], None]]] = {}

    def subscribe(self, event_type: EventType, handler: Callable[[GameEventException], None]) -> None:
        """
        Subscribes a handler to an event type.

        Args:
            event_type (EventType): The event type to subscribe to.
            handler (Callable[[GameEventException], None]): The event handler to subscribe.
        """
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []

        self._subscribers[event_type].append(handler)

    def unsubscribe(self, event_type: EventType, handler: Callable[[GameEventException], None]) -> None:
        """
        Unsubscribes a handler from an event type.

        Args:
            event_type (EventType): The event type to unsubscribe from.
            handler (Callable[[GameEventException], None]): The event handler to unsubscribe.
        """
        if event_type in self._subscribers:
            try:
                self._subscribers[event_type].remove(handler)

                if not self._subscribers[event_type]:
                    del self._subscribers[event_type]
            except ValueError:
                print(f"There is no handler registered for event type {event_type}")

    def dispatch(self, event: GameEventException) -> None:
        """
        Dispatches an event to all registered handlers.

        Args:
           event (GameEventException): The event to dispatch.
        """
        handlers = self._subscribers.get(event.event_type, [])

        for handler in handlers:
            handler(event)
