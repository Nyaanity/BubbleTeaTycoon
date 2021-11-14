class Events:
    """Base class for events."""

    def __init__(self):
        super().__init__()
        self.__event_listeners = []

    def dispatch(self, event, *args, **kwargs):
        actual_event = 'on_' + event
        for listener in self.__event_listeners:
            if listener.__name__ == actual_event:
                return listener(*args, **kwargs)

    def observer(self):
        def wrapper(func):
            self.__event_listeners.append(func)
        return wrapper


e = Events()


@e.observer()
def on_ready(a, b):
    print("redy")
    
    
e.dispatch('ready', 1,2)
