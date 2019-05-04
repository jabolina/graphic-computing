import pygame

from illustrator import BaseIllustrator
from illustrator.bucket import Bucket
from illustrator.circle import CircleIllustrator
from illustrator.curve import CurveIllustrator
from illustrator.line import LineIllustrator
from illustrator.polyline import PolylineIllustrator
from illustrator.rectangle import RectangleIllustrator
from illustrator.square import SquareIllustrator
from user_interface.constants import WHITE
from user_interface.context import GUIContext, OptionsContext, DrawContext
from user_interface.utils import available_options


class IllustratorContext:
    """
        This class will hold all the references to the illustrator classes
    """

    def __init__(self, gui_context: GUIContext, gui_options: OptionsContext):
        """
            If you look closely, the illustrator classes follows the
            same sequence defined in utils.available_options
        :param gui_context:
        :param gui_options:
        """
        self.illustrators = [
            LineIllustrator(gui_context, gui_options),
            RectangleIllustrator(gui_context, gui_options),
            SquareIllustrator(gui_context, gui_options),
            PolylineIllustrator(gui_context, gui_options),
            CurveIllustrator(gui_context, gui_options),
            CircleIllustrator(gui_context, gui_options),
            Bucket(gui_context, gui_options),
        ]


class GUIEventHandler:
    def __init__(self):
        pygame.init()
        self.options_context = OptionsContext()
        self.gui_context = GUIContext()
        self.gui_context.screen.fill(WHITE)
        self.illustrator = IllustratorContext(
            self.gui_context,
            self.options_context
        )

    def _color_change(self, value: tuple) -> None:
        self.options_context.line_color = value

    def _option_to_illustrator(self, option: str) -> BaseIllustrator:
        return self.illustrator.illustrators[available_options().index(option)]

    def on_rect_click(self, draw: DrawContext) -> bool:
        """
            Verify if the pressed item is a color element or an
            option element and handle it accordingly
        :param draw: The pressed element in context, with element surface and position
        :return success or fail
        """
        print('The pressed element: ', draw.element)

        if draw.kwargs.get("is_color"):
            self._color_change(draw.element.get_at((0, 0)))
            return True

        illustrator = self._option_to_illustrator(draw.kwargs.get("value"))

        if isinstance(illustrator, CircleIllustrator):
            illustrator.draw_circle(option_position=draw.position)
        elif isinstance(illustrator, Bucket):
            illustrator.bucket_paint()
        else:
            illustrator.draw_line(option_position=draw.position)

        return True
