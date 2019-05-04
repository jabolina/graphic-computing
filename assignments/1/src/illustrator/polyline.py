import pygame
from typing import List, Tuple

from pygame.constants import QUIT, KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP

from illustrator.point import PointContext
from user_interface import DrawContext
from user_interface.constants import DEFAULT_DIMENSION
from user_interface.utils import green, blue, draw_to_surface
from . import BaseIllustrator


class PolylineIllustrator(BaseIllustrator):
    def draw(self, control_points: List[Tuple]) -> DrawContext:
        polyline_surface = pygame.Surface(DEFAULT_DIMENSION, pygame.SRCALPHA, 32)
        polyline_surface.convert_alpha()

        if len(control_points):
            for start, end in zip(control_points[0:], control_points[1:]):
                self._bresenham(start, end, polyline_surface)

        polyline_context = DrawContext(polyline_surface, (0, 0))
        polyline_context.is_valid = False

        return polyline_context

    def draw_line(self, *args, **kwargs):
        """
            The user will add new point with the right mouse button
            Will drag the points with the left mouse button
            And press any key on keyboard to leave
        :param args: anything
        :param kwargs: anything
        """
        control_points: List[PointContext] = []
        original_position = kwargs.get('option_position')
        is_running = True
        selected: PointContext = None
        clock = pygame.time.Clock()

        while is_running:
            context = self.draw([(p.x, p.y) for p in control_points])
            surface = context.element

            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    is_running = False

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for point in control_points:
                            if abs(point.x - event.pos[0]) < 10 and abs(point.y - event.pos[1]) < 10:
                                selected = point
                    elif event.button == 3 and event.pos != original_position:
                        control_points.append(PointContext(event.pos))

                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    selected = None

            if selected is not None:
                selected.x, selected.y = pygame.mouse.get_pos()
                pygame.draw.circle(surface, green, (selected.x, selected.y), 10)

            for point in control_points:
                pygame.draw.circle(surface, blue, (point.x, point.y), 10)

            draw_to_surface(self.gui_context.screen, [context, *self.gui_context.draw_surfaces])

            clock.tick(100)

        self.gui_context.draw_surfaces = self.draw([(p.x, p.y) for p in control_points])

    def draw_circle(self, *args, **kwargs):
        pass
