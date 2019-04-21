from typing import List, Tuple

import pygame

from user_interface.constants import BLACK, LINE_SIZE, DEFAULT_DIMENSION


class DrawContext:
    def __init__(self, element: pygame.Surface, position: Tuple[int, int], *args, **kwargs):
        self._element = element
        self._position = position
        self._is_valid = True
        self.args = args
        self.kwargs = kwargs

    @property
    def element(self) -> pygame.Surface:
        return self._element

    @property
    def position(self) -> Tuple[int, int]:
        return self._position

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value


class OptionsContext:
    def __init__(self):
        self._keep_running = True
        self._line_color = BLACK
        self.line_size = LINE_SIZE

    @property
    def line_color(self):
        return self._line_color

    @line_color.setter
    def line_color(self, color):
        self._line_color = color

    @property
    def keep_running(self):
        return self._keep_running

    @keep_running.setter
    def keep_running(self, value):
        self._keep_running = value


class GUIContext:
    def __init__(self):
        self._screen = pygame.display.set_mode(DEFAULT_DIMENSION)
        self._text_generator = pygame.font.SysFont('Arial', 18)
        self._background = pygame.Surface(DEFAULT_DIMENSION)
        self._draw_surfaces: List[DrawContext] = []

    @property
    def screen(self):
        return self._screen

    @property
    def text_generator(self):
        return self._text_generator

    @property
    def background(self):
        return self._background

    @property
    def draw_surfaces(self):
        return self._draw_surfaces

    @draw_surfaces.setter
    def draw_surfaces(self, draw: DrawContext):
        self._draw_surfaces.insert(0, draw)
        # self._draw_surfaces.append(draw)
