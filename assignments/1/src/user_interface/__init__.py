from typing import List, Tuple

import pygame

from user_interface.constants import BLACK, DEFAULT_WIDTH, DEFAULT_HEIGHT
from user_interface.context import DrawContext
from user_interface.event_handler import GUIEventHandler
from user_interface.utils import palette_colors, available_options


class UserInterface(GUIEventHandler):
    def __init__(self):
        """
            Entry point, holds the GUI context and the user options context
        """
        super().__init__()
        pygame.display.set_caption("Paint")

    @staticmethod
    def draw_to_surface(surface: pygame.Surface, elements: List[DrawContext]):
        for element in elements:
            surface.blit(element.element, element.position)

    @staticmethod
    def surface_was_pressed(draw: DrawContext, mouse_position: Tuple[int, int]) -> bool:
        element = draw.element
        (x, y) = draw.position
        (height, width) = element.get_size()
        (m, n) = mouse_position

        return (x <= m <= (x + height)) and (y <= n <= (y + width))

    def create_options(self):
        """
            Keep drawing the options available for the user to choose,
            from left top to left bottom
        """
        options = available_options()

        for idx, option in enumerate(options):
            option_surface = pygame.Surface((60, 25))
            option_surface.fill((155, 155, 155))
            position = (5, 28 * (idx + 1))
            text = self.gui_context.text_generator.render(option, True, BLACK)
            option_surface.blit(text, (0, 5))
            self.gui_context.draw_surfaces = DrawContext(option_surface, position, is_color=False, value=option)

    def create_color_palette(self):
        """
            Keep drawing the color palette in the top of screen, from
            left to right
        """
        colors = palette_colors()

        for idx, available_color in enumerate(colors):
            color_surface = pygame.Surface((20, 20))
            color_surface.fill(available_color)
            position = (20 * idx, 0)
            self.gui_context.draw_surfaces = DrawContext(color_surface, position, is_color=True)

    def handle_pressed_element(self, elements: List[DrawContext]):
        """
            Will handle the pressed color or option. If color, change the
            color in use, if one of the tools is selected, the user will have
            the option to draw.
        :param elements: List of pressed element
        """
        [self.on_rect_click(element) for element in elements]

    def run(self):
        """
            Keeps running until the quit button is pressed and the
            application ends. Will draw the color palette, and options, keeps
            looking for pressed elements in the screen.
        :return:
        """

        self.create_color_palette()
        self.create_options()

        while self.options_context.keep_running:
            UserInterface.draw_to_surface(self.gui_context.screen, self.gui_context.draw_surfaces)

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.options_context.keep_running = False

                mouse_position = pygame.mouse.get_pos()
                is_pressed, _, __ = pygame.mouse.get_pressed()

                if is_pressed:
                    self.handle_pressed_element([draw for draw in
                                                 self.gui_context.draw_surfaces if
                                                 UserInterface.surface_was_pressed(
                                                     draw,
                                                     mouse_position
                                                 )])

            pygame.display.flip()
