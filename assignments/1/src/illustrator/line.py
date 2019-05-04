from typing import List, Tuple

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from user_interface.constants import DEFAULT_DIMENSION
from user_interface.context import DrawContext
from user_interface.utils import draw_to_surface
from . import BaseIllustrator


class LineIllustrator(BaseIllustrator):
    def draw_line(self, *args, **kwargs) -> None:
        """
            Will keep awaiting for two mouse clicks, the position where
            it will start and another click where the line ends
        :param args:
        :param kwargs:
        """
        control_points: List[Tuple[int, int]] = []
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            event = pygame.event.wait()

            if not len(control_points):
                if event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    is_pressed, _, __ = pygame.mouse.get_pressed()

                    if is_pressed:
                        control_points.append(mouse_position)
            else:
                mouse_position = pygame.mouse.get_pos()
                line_surface: pygame.Surface = pygame.Surface(DEFAULT_DIMENSION, pygame.SRCALPHA, 32)
                line_surface.convert_alpha()
                self._bresenham(control_points[0], mouse_position, line_surface)
                line_context = DrawContext(line_surface, (0, 0))
                line_context.is_valid = False
                draw_to_surface(self.gui_context.screen, [line_context, *self.gui_context.draw_surfaces])

                if event.type == MOUSEBUTTONDOWN:
                    is_running = False
                    self.gui_context.draw_surfaces = line_context

            clock.tick(100)

    def draw_circle(self, *args, **kwargs) -> None:
        pass
