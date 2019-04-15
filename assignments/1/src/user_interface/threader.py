import asyncio
from threading import Thread
from typing import Callable, Awaitable


class CoroutineThreader(Thread):
    """
        If all the drawing methods were marked as `async`, then they could
        be executed in a separated thread, maybe this is just complicating
        this too much, but who knows?
    """
    def __init__(self, coroutine: Callable[[tuple], Awaitable[None]],
                 *args, **kwargs):
        super().__init__()
        self._callback = coroutine
        self.args = args
        self.kwargs = kwargs

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._callback(*self.args, **self.kwargs))
        loop.close()


class RoutineThreader(Thread):
    """
        This will launch a method in another thread, this is for methods
        that are no `async` marked
    """
    def __init__(self, method: Callable, *args, **kwargs):
        super().__init__()
        self.callback = method
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.callback(*self.args, **self.kwargs)
