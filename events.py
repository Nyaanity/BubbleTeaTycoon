class Events:
    """Base class for events."""

    def __init__(self):
        super().__init__()
        self.__event_listeners = []

    async def dispatch(self, event, *args, **kwargs):
        """Dispatches an event."""
        actual_event = 'on_' + event
        for listener in self.__event_listeners:
            if listener.__name__ == actual_event:
                return await listener(*args, **kwargs)

    def observer(self):
        """Marks a function to be a listener."""
        def wrapper(func):
            self.__event_listeners.append(func)
        return wrapper
