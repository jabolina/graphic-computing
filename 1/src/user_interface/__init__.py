import pygame

from user_interface.utils import palette_colors, available_options

DEFAULT_DIMENSION = (1024, 768)
LINE_SIZE = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Context(object):
    def __init__(self):
        self._keep_running = True
        self._line_color = BLACK
        self._elements = []
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


class UserInterface:
    def __init__(self):
        pygame.init()

        self.context = Context()
        self.screen = pygame.display.set_mode(DEFAULT_DIMENSION)
        self.text_generator = pygame.font.SysFont('Arial', 18)
        self.background = pygame.Surface(DEFAULT_DIMENSION)

        self.screen.fill(WHITE)
        pygame.display.set_caption("Paint")

    def draw_options(self):
        options = available_options()

        for idx, option in enumerate(options):
            text = self.text_generator.render(option, True, BLACK)
            self.context.elements = \
                self.screen.blit(text, (5, 25 * idx))

    def draw_color_palette(self):
        colors = palette_colors()

        for idx, available_color in enumerate(colors):
            self.context.elements = \
                pygame.draw.rect(self.screen,
                                 available_color,
                                 [20 * idx, 0, 20, 20])

    def handle_pressed_element(self, element: pygame.Rect):
        """
            Will handle the pressed color or option. If color, change the color in use,
            if one of the tools is selected, the user will have the option to draw.
        :param element: Pressed element
        """

    def run(self):
        while self.context.keep_running:
            self.draw_options()
            self.draw_color_palette()

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.context.keep_running = False

                mouse_position = pygame.mouse.get_pos()
                is_pressed, _, __ = pygame.mouse.get_pressed()

                pressed_elements = [element for element in
                                    self.context.elements if
                                    element.collidepoint(mouse_position) and is_pressed]

                print(pressed_elements)

            del self.context.elements
            pygame.display.flip()
