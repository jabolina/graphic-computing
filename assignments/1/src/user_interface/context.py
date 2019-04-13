import pygame
from user_interface.constants import BLACK, LINE_SIZE, DEFAULT_DIMENSION


class OptionsContext:
    def __init__(self):
        self._keep_running = True
        self._line_color = BLACK
        self._elements = []
        self._element_in_position = []
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

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, element):
        self.elements.append(element)

    @elements.deleter
    def elements(self):
        self.elements.clear()

    @property
    def element_in_position(self):
        return self._element_in_position

    @element_in_position.setter
    def element_in_position(self, element):
        self._element_in_position.append(element)

    @element_in_position.deleter
    def element_in_position(self):
        self._element_in_position.clear()


class GUIContext:
    def __init__(self):
        self._screen = pygame.display.set_mode(DEFAULT_DIMENSION)
        self._text_generator = pygame.font.SysFont('Arial', 18)
        self._background = pygame.Surface(DEFAULT_DIMENSION)

    @property
    def screen(self):
        return self._screen

    @property
    def text_generator(self):
        return self._text_generator

    @property
    def background(self):
        return self._background
