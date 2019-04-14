import pygame

from . import BaseIllustrator


class LineIllustrator(BaseIllustrator):
    def draw_line(self, *args, **kwargs) -> None:
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
        self._bresenham(*positions[0], *positions[1])

    def draw_circle(self, *args, **kwargs) -> None:
        print("How the hell did you get here???")
