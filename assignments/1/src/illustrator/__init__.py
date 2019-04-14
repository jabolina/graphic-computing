import abc
from typing import Tuple

import pygame

from user_interface.context import GUIContext, OptionsContext

PIXEL_SIZE = 1


class BaseIllustrator:
    __metaclass__ = abc.ABCMeta

    def __init__(self, gui_context: GUIContext,
                 options_context: OptionsContext):
        self.gui_context = gui_context
        self.options_context = options_context

    def _set_pixel(self, x, y):
        self.gui_context.screen.set_at((x, y), self.options_context.line_color)

    def _bresenham(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0

        if dy < 0:
            dy = -dy
            stepy = -1
        else:
            stepy = 1

        if dx < 0:
            dx = -dx
            stepx = -1
        else:
            stepx = 1

        dx <<= 2
        dy <<= 2

        self._set_pixel(x0, y0)

        if dx > dy:
            fraction = dy - (dx >> 1)
            while x0 != x1:
                if fraction >= 0:
                    y0 += stepy
                    fraction -= dx
                x0 += stepx
                fraction += dy
                self._set_pixel(x0, y0)
        else:
            fraction = dx - (dy >> 1)
            while y0 != y1:
                if fraction >= 0:
                    x0 += stepx
                    fraction -= dy
                y0 += stepy
                fraction += dx
                self._set_pixel(x0, y0)

        pygame.display.flip()

    def _middle_point(self, radius: int, center: Tuple[int, int]) -> None:
        x0, y0 = center
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius

        x = 0
        y = radius

        self._set_pixel(x0, y0 + radius)
        self._set_pixel(x0, y0 - radius)
        self._set_pixel(x0 + radius, y0)
        self._set_pixel(x0 - radius, y0)

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x

            self._set_pixel(x0 + x, y0 + y)
            self._set_pixel(x0 - x, y0 + y)
            self._set_pixel(x0 + x, y0 - y)
            self._set_pixel(x0 - x, y0 - y)
            self._set_pixel(x0 + y, y0 + x)
            self._set_pixel(x0 - y, y0 + x)
            self._set_pixel(x0 + y, y0 - x)
            self._set_pixel(x0 - y, y0 - x)

        pygame.display.flip()

    @abc.abstractmethod
    def draw_line(self, *args, **kwargs):
        """
            Method must be implemented, this will draw single lines
        :param args: Anything
        :param kwargs: Anything
        """
        raise NotImplementedError

    @abc.abstractmethod
    def draw_circle(self, *args, **kwargs):
        """
            Method must be implemented, this will draw circles
        :param args: Anything
        :param kwargs: Anything
        """
        raise NotImplementedError
