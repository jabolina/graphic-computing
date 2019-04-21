import abc
from math import sqrt
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

    @staticmethod
    def get_surface_size(begin: Tuple[int, int], end: Tuple[int, int]) -> Tuple[float, float]:
        x0, y0 = begin
        x1, y1 = end

        return abs(sqrt((x0 - x1) ** 2)), abs(sqrt((y0 - y1) ** 2))

    @staticmethod
    def get_surface_start(first: Tuple[int, int], now: Tuple[int, int]) -> Tuple[int, int]:
        x0, y0 = first
        x1, y1 = now
        point = x0, y0

        if x1 < x0:
            point = x1, point[1]

        if y1 < y0:
            point = point[0], y1

        return point

    def _set_pixel(self, x, y, surface: pygame.Surface):
        surface.set_at((x, y), self.options_context.line_color)

    def _bresenham(self, start: Tuple[int, int], end: Tuple[int, int], surface: pygame.Surface):
        x0, y0 = start
        x1, y1 = end
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

        self._set_pixel(x0, y0, surface)

        if dx > dy:
            fraction = dy - (dx >> 1)
            while x0 != x1:
                if fraction >= 0:
                    y0 += stepy
                    fraction -= dx
                x0 += stepx
                fraction += dy
                self._set_pixel(x0, y0, surface)
        else:
            fraction = dx - (dy >> 1)
            while y0 != y1:
                if fraction >= 0:
                    x0 += stepx
                    fraction -= dy
                y0 += stepy
                fraction += dx
                self._set_pixel(x0, y0, surface)

        pygame.display.flip()

    def _middle_point(self, radius: int, center: Tuple[int, int], surface: pygame.Surface) -> None:
        x0, y0 = center
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius

        x = 0
        y = radius

        self._set_pixel(x0, y0 + radius, surface)
        self._set_pixel(x0, y0 - radius, surface)
        self._set_pixel(x0 + radius, y0, surface)
        self._set_pixel(x0 - radius, y0, surface)

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x

            self._set_pixel(x0 + x, y0 + y, surface)
            self._set_pixel(x0 - x, y0 + y, surface)
            self._set_pixel(x0 + x, y0 - y, surface)
            self._set_pixel(x0 - x, y0 - y, surface)
            self._set_pixel(x0 + y, y0 + x, surface)
            self._set_pixel(x0 - y, y0 + x, surface)
            self._set_pixel(x0 + y, y0 - x, surface)
            self._set_pixel(x0 - y, y0 - x, surface)

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
