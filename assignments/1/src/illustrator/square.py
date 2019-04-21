from typing import Tuple, List

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from user_interface.constants import DEFAULT_DIMENSION
from user_interface.context import DrawContext
from user_interface.utils import draw_to_surface
from . import BaseIllustrator


class SquareIllustrator(BaseIllustrator):
    @staticmethod
    def transform_coordinates(upper: Tuple[int, int], bottom: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
            With the upper left and bottom right position, will
            create the 4 needed coordinates to draw the complete object

        :param upper: Upper left coordinates (x, y)
        :param bottom: Bottom right coordinates (x, y)
        :return: A list with the four coordinates
        """
        x1, y1 = upper
        x2, y2 = bottom

        return [upper, (x1, y2), (x2, y1), bottom]

    def draw_line(self, *args, **kwargs):
        """
            The user will choose two points, the start and end of the square/rectangle:

                (x, y) - - - - - - 0
                  |                |
                  |                |
                  |                |
                  |                |
                  |                |
                  0 - - - - - - (x, y)

            Then the object will be drawn
        :param args: anything
        :param kwargs: anything
        """
        control_point: Tuple[int, int] = None
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            event = pygame.event.wait()

            if control_point is None:
                if event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    is_pressed, _, __ = pygame.mouse.get_pressed()

                    if is_pressed:
                        control_point = mouse_position
            else:
                mouse_position = pygame.mouse.get_pos()
                square_surface: pygame.Surface = pygame.Surface(DEFAULT_DIMENSION, pygame.SRCALPHA, 32)
                square_surface.convert_alpha()

                [u_l, u_r, b_l, b_r] = SquareIllustrator.transform_coordinates(control_point, mouse_position)
                self._bresenham(u_l, u_r, square_surface)
                self._bresenham(u_l, b_l, square_surface)
                self._bresenham(b_l, b_r, square_surface)
                self._bresenham(u_r, b_r,square_surface)

                square_context = DrawContext(square_surface, (0, 0))
                square_context.is_valid = False
                draw_to_surface(self.gui_context.screen, [square_context, *self.gui_context.draw_surfaces])

                if event.type == MOUSEBUTTONDOWN:
                    is_running = False
                    self.gui_context.draw_surfaces = square_context

            clock.tick(100)

    def draw_circle(self, *args, **kwargs):
        print("Draw circle")
