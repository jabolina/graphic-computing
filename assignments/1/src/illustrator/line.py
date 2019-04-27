from typing import Tuple

import pygame
from pygame.constants import MOUSEBUTTONDOWN

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
                surface_size = BaseIllustrator.get_surface_size(control_point, mouse_position)
                surface_start = BaseIllustrator.get_surface_start(control_point, mouse_position)

                line_surface: pygame.Surface = pygame.Surface(surface_size, pygame.SRCALPHA, 32)
                line_surface.convert_alpha()

                root = BaseIllustrator.translate_coordinates(control_point, surface_start)
                position = BaseIllustrator.translate_coordinates(mouse_position, surface_start)

                self._bresenham(root, position, line_surface)
                line_context = DrawContext(line_surface, surface_start)
                line_context.is_valid = False

                draw_to_surface(self.gui_context.screen, [line_context, *self.gui_context.draw_surfaces])

                if event.type == MOUSEBUTTONDOWN:
                    is_running = False
                    self.gui_context.draw_surfaces = line_context

            clock.tick(120)

    def draw_circle(self, *args, **kwargs) -> None:
        print("How the hell did you get here???")
