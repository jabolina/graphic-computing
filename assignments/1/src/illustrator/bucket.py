from typing import Tuple

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from illustrator import BaseIllustrator
from user_interface import DrawContext
from user_interface.constants import DEFAULT_DIMENSION, WHITE
from user_interface.utils import merge_surfaces, draw_to_surface


class Bucket(BaseIllustrator):
    def draw_line(self, *args, **kwargs):
        pass

    def draw_circle(self, *args, **kwargs):
        pass

    def is_invalid(self, surface_array: pygame.PixelArray,
                   position: Tuple[int, int]) -> bool:
        max_x, max_y = DEFAULT_DIMENSION
        x, y = position
        color = self.options_context.line_color

        return x < 0 or y < 0 or x >= max_x or y >= max_y \
            or surface_array[x][y] == color

    def is_valid(self, surf: pygame.Surface, position: Tuple[int, int]) -> bool:
        max_x, max_y = DEFAULT_DIMENSION
        x, y = position
        color = self.options_context.line_color
        print((0 < x < max_x) and (0 < y < max_y) and surf.get_at(position) != color and surf.get_at(position) == WHITE)
        return (0 < x < max_x) and (0 < y < max_y) and surf.get_at(position) != color and surf.get_at(position) == WHITE

    def _iter_flood_fill(self, surface: pygame.Surface,
                         position: Tuple[int, int]) -> pygame.Surface:

        clock = pygame.time.Clock()
        color = self.options_context.line_color
        points = [position]

        while len(points) > 0:
            (x, y), *points = points
            print(len(points), x, y)
            surface.set_at((x, y), color)

            if self.is_valid(surface, (x + 1, y)):
                points.append((x + 1, y))

            if self.is_valid(surface, (x - 1, y)):
                points.append((x - 1, y))

            if self.is_valid(surface, (x, y + 1)):
                points.append((x, y + 1))

            if self.is_valid(surface, (x, y - 1)):
                points.append((x, y - 1))

            color_context = DrawContext(surface, (0, 0))
            color_context.is_valid = False

            draw_to_surface(self.gui_context.screen, [color_context, *self.gui_context.draw_surfaces])

            pygame.display.flip()
            clock.tick(100)

        return surface

    def bucket_paint(self, *args, **kwargs) -> None:
        """
            Will receive a click on the screen, then will merge ALL surfaces
            together into one. After this happen, the click will grow like
            a rock in a water, when the water grow from a stress point outwards

        :param args: Anything
        :param kwargs: Anything
        """
        control_point: Tuple[int, int] = None

        while control_point is None:
            event = pygame.event.wait()

            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                is_pressed, _, __ = pygame.mouse.get_pressed()

                if is_pressed:
                    control_point = mouse_position

        merged_context = merge_surfaces([i for i in self.gui_context.draw_surfaces if not i.is_valid])
        del self.gui_context.draw_surfaces

        painted = self._iter_flood_fill(merged_context.element, control_point)

        merged_context.element = painted
        self.gui_context.draw_surfaces = merged_context
