from typing import List, Tuple

import pygame
from math import sqrt

from pygame.constants import MOUSEBUTTONDOWN

from user_interface.context import DrawContext
from user_interface.utils import draw_to_surface
from user_interface.constants import DEFAULT_DIMENSION
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
                circle_suface: pygame.Surface = pygame.Surface(DEFAULT_DIMENSION, pygame.SRCALPHA, 32)
                circle_suface.convert_alpha()

                radius = CircleIllustrator.find_radius(control_point, mouse_position)
                self._middle_point(radius, mouse_position, circle_suface)
                line_context = DrawContext(circle_suface, (0, 0))
                line_context.is_valid = False
                draw_to_surface(self.gui_context.screen, [line_context, *self.gui_context.draw_surfaces])

                if event.type == MOUSEBUTTONDOWN:
                    is_running = False
                    self.gui_context.draw_surfaces = line_context

            clock.tick(100)
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
"""
    @staticmethod
    def find_radius(center: tuple, border: tuple) -> int:
        x1, y1 = center
        x2, y2 = border
        return int(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
