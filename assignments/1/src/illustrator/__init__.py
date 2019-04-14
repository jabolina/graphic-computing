import pygame
import abc
from pygame import gfxdraw

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

    def _symmetry_points(self, x, y, offset):
        gfxdraw.pixel(self.gui_context.screen, x + offset,
                      y + offset, self.options_context.line_color)
        gfxdraw.pixel(self.gui_context.screen, -x + offset,
                      y + offset, self.options_context.line_color)
        gfxdraw.pixel(self.gui_context.screen, x + offset,
                      -y + offset, self.options_context.line_color)
        gfxdraw.pixel(self.gui_context.screen, -x + offset,
                      -y + offset, self.options_context.line_color)
        gfxdraw.pixel(self.gui_context.screen, y + offset,
                      x + offset, self.options_context.line_color)
        gfxdraw.pixel(self.gui_context.screen, -y + offset,
                      x + offset, self.options_context.line_color)
        gfxdraw.pixel(self.gui_context.screen, y + offset,
                      -x + offset, self.options_context.line_color)
        gfxdraw.pixel(self.gui_context.screen, -y + offset,
                      -x + offset, self.options_context.line_color)

        pygame.display.flip()

    def _plot_circle(self, x, y, radius, offset):
        d = 5 / 4.0 - radius
        self._symmetry_points(x, y, offset)

        while x < y:
            if d < 0:
                x += 1
                d += 2 * x + 1
            else:
                x += 1
                y -= 1
                d += 2 * (x - y) + 1

            self._symmetry_points(x, y, radius + offset)

    def _middle_point(self, radius, offset):
        x, y = 0, radius
        self._plot_circle(x, y, radius, offset)

    @abc.abstractmethod
    def draw_line(self, *args, **kwargs):
        """
            Method must be implemented, this will draw single lines
        :param args: Anything
        :param kwargs: Anythin
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
