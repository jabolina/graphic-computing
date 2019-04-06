import pygame
from pygame import gfxdraw

from user_interface import GUIContext, OptionsContext


class BaseIllustrator(object):
    def __init__(self, gui_context: GUIContext,
                 options_context: OptionsContext):
        self.gui_context = gui_context
        self.options_context = options_context

    def bresenham(self, x_points, y_points):
        x1, x2 = x_points
        y1, y2 = y_points

        dx = x2 - x1
        dy = y2 - y1

        d = 2 * dy - dx

        gfxdraw.pixel(self.gui_context.screen, x1,
                      y1, self.options_context.line_color)

        y = y1

        for x in range(x1 + 1, x2 + 1):
            if d > 0:
                y += 1
                gfxdraw.pixel(self.gui_context.screen, x,
                              y, self.options_context.line_color)
                d += 2 * dy - 2 * dx
            else:
                gfxdraw.pixel(self.gui_context.screen, x,
                              y, self.options_context.line_color)
                d += 2 * dy

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
                d += 2*x + 1
            else:
                x += 1
                y -= 1
                d += 2 * (x - y) + 1

            self._symmetry_points(x, y, radius + offset)

    def middle_point(self, radius, offset):
        x, y = 0, radius
        self._plot_circle(x, y, radius, offset)
