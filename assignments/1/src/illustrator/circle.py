import pygame
from math import sqrt

from . import BaseIllustrator


class CircleIllustrator(BaseIllustrator):
    def draw_line(self, *args, **kwargs):
        print('How the hell did you get here???')

    def draw_circle(self, *args, **kwargs):
        """
            Will keep awaiting for two mouse clicks, the position where
            it will start and another click where the line ends
        :param args:
        :param kwargs:
        """
        positions = []
        original_position = kwargs.get('option_position')

        while len(positions) < 2:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                is_pressed, _, __ = pygame.mouse.get_pressed()

                if is_pressed and mouse_position != original_position:
                    positions.append(mouse_position)

        print('Start: ', positions[0])
        print('End: ', positions[1])
        radius = CircleIllustrator.find_radius(positions[0], positions[1])
        self._middle_point(radius, positions[0])

    @staticmethod
    def find_radius(center: tuple, border: tuple) -> int:
        x1, y1 = center
        x2, y2 = border
        return int(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
