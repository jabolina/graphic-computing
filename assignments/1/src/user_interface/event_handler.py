from threading import Thread
from typing import Callable, Awaitable

import asyncio
import pygame

from illustrator import BaseIllustrator
from illustrator.circle import CircleIllustrator
from illustrator.curve import CurveIllustrator
from illustrator.line import LineIllustrator
from illustrator.polyline import PolylineIllustrator
from illustrator.rectangle import RectangleIllustrator
from illustrator.square import SquareIllustrator
from user_interface.context import GUIContext, OptionsContext
from user_interface.utils import available_options
from user_interface.constants import WHITE


class IllustratorContext:
    """
        This class will hold all the references to the illustrator classes
    """

    def __init__(self, gui_context: GUIContext, gui_options: OptionsContext):
        """
            If you look closely, the illustrator classes follows the same sequence
            defined in utils.available_options
        :param gui_context:
        :param gui_options:
        """
        self.illustrators = [
            LineIllustrator(gui_context, gui_options),
            RectangleIllustrator(gui_context, gui_options),
            SquareIllustrator(gui_context, gui_options),
            PolylineIllustrator(gui_context, gui_options),
            CurveIllustrator(gui_context, gui_options),
            CircleIllustrator(gui_context, gui_options)
        ]


class Threader(Thread):
    """
        If all the drawing methods were marked as `async`, then they could be executed
        in a separated thread, maybe this is just complicating this too much, but who knows?
    """
    def __init__(self, coroutine: Callable[[tuple], Awaitable[None]], *args, **kwargs):
        super().__init__()
        self._callback = coroutine
        self.args = args
        self.kwargs = kwargs

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._callback(*self.args, **self.kwargs))
        loop.close()


class GUIEventHandler:
    def __init__(self):
        pygame.init()
        self.options_context = OptionsContext()
        self.gui_context = GUIContext()
        self.gui_context.screen.fill(WHITE)
        self.illustrator = IllustratorContext(self.gui_context, self.options_context)

    def _color_change(self, value: tuple) -> None:
        self.options_context.line_color = value

    def _option_to_illustrator(self, option: str) -> BaseIllustrator:
        return self.illustrator.illustrators[available_options().index(option)]

    def on_rect_click(self, element: pygame.Rect, element_info: dict) -> bool:
        """
            Verify if the pressed item is a color element or an
            option element and handle it accordingly
        :param element: The pressed rect element
        :param element_info: Information about the pressed element
        :return success or fail
        """
        print('The pressed element: ', element)
        print('Information about: ', element_info)
        if element_info['is_color']:
            self._color_change(element_info['value'])
            return True

        illustrator = self._option_to_illustrator(element_info['value'])

        if isinstance(illustrator, CircleIllustrator):
            # complete_in_future = Threader(illustrator.draw_circle, option_position=element_info['position'])
            illustrator.draw_circle(option_position=element_info['position'])
        else:
            # complete_in_future = Threader(illustrator.draw_line, option_position=element_info['position'])
            illustrator.draw_line(option_position=element_info['position'])

        # If pygame had support for multi threading, this could be done :/
        # complete_in_future.start()
        return True
