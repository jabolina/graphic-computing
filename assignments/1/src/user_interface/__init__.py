import pygame

from typing import List

from user_interface.constants import BLACK, LINE_SIZE, DEFAULT_DIMENSION
from user_interface.event_handler import GUIEventHandler
from user_interface.utils import palette_colors, available_options


class UserInterface(GUIEventHandler):
    def __init__(self):
        """
            Entry point, holds the GUI context and the user options context
        """
        super().__init__()
        pygame.display.set_caption("Paint")

    def draw_options(self):
        """
            Keep drawing the options available for the user to choose,
            from left top to left bottom
        """
        options = available_options()

        for idx, option in enumerate(options):
            position = (5, 25 * (idx + 1))
            self.options_context.element_in_position = {
                'is_color': False,
                'value': option,
                'position': position
            }
            text = self.gui_context.text_generator.render(option, True, BLACK)
            self.options_context.elements = \
                self.gui_context.screen.blit(text, position)

    def draw_color_palette(self):
        """
            Keep drawing the color palette in the top of screen, from
            left to right
        """
        colors = palette_colors()

        for idx, available_color in enumerate(colors):
            self.options_context.element_in_position = {
                'is_color': True,
                'value': available_color,
                'position': (20 * idx, 0)
            }
            self.options_context.elements = \
                pygame.draw.rect(self.gui_context.screen,
                                 available_color,
                                 [20 * idx, 0, 20, 20])

    def handle_pressed_element(self, elements: List[pygame.Rect]):
        """
            Will handle the pressed color or option. If color, change the
            color in use, if one of the tools is selected, the user will have
            the option to draw.
        :param elements: List of pressed element
        """
        for information in self.options_context.element_in_position:
            [self.on_rect_click(element, information)
             if element.collidepoint(*information['position'])
             else ''
             for element in elements]

    def run(self):
        """
            Keeps running until the quit button is pressed and the
            application ends. Will draw the color palette, and options, keeps
            looking for pressed elements in the screen.
        :return:
        """
        while self.options_context.keep_running:
            self.draw_options()
            self.draw_color_palette()

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.options_context.keep_running = False

                mouse_position = pygame.mouse.get_pos()
                is_pressed, _, __ = pygame.mouse.get_pressed()

                self.handle_pressed_element([element for element in
                                             self.options_context.elements if
                                             element.collidepoint(
                                                 mouse_position
                                             ) and
                                             is_pressed])

            del self.options_context.elements
            del self.options_context.element_in_position
            pygame.display.flip()
