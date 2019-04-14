from typing import Tuple, List

import pygame

from . import BaseIllustrator


class RectangleIllustrator(BaseIllustrator):
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
        positions: List[Tuple[int, int]] = []
        original_position = kwargs.get('option_position')

        while len(positions) < 2:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                is_pressed, _, __ = pygame.mouse.get_pressed()

                if is_pressed and mouse_position != original_position:
                    positions.append(mouse_position)

        [u_l, u_r, b_l, b_r] = RectangleIllustrator.transform_coordinates(*positions)
        self._bresenham(*u_l, *u_r)
        self._bresenham(*u_l, *b_l)
        self._bresenham(*b_l, *b_r)
        self._bresenham(*u_r, *b_r)

    def draw_circle(self, *args, **kwargs):
        print("How the hell did you get here?????")
