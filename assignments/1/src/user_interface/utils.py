from typing import List

import pygame

from user_interface import DrawContext
from user_interface.constants import WHITE, DEFAULT_DIMENSION

lightgray = (200, 200, 200)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
pink = (255, 0, 255)
red_brown = (128, 64, 64)
yellow = (255, 255, 0)
purple = (128, 0, 128)
mustard = (128, 128, 0)
light_blue = (0, 255, 255)
ocean_blue = (0, 128, 255)
blue_green = (0, 128, 128)
green_gray = (77, 91, 66)
gray = (128, 128, 128)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 128, 0)


def palette_colors():
    return [
        red,
        pink,
        red_brown,
        yellow,
        purple,
        mustard,
        blue,
        light_blue,
        ocean_blue,
        blue_green,
        green,
        green_gray,
        gray,
        black,
        white,
        orange
    ]


def available_options():
    """
        The sequence defined here is the same as the illustrator sequence
        defined in the IllustratorContext, this is needed to know which
        option was pressed

    :return: list of available options to the user
    """
    return [
        'Linha',
        'Retangulo',
        'Quadrado',
        'Polilinha',
        'Curva',
        'Circulo',
        'Balde'
    ]


def draw_to_surface(surface: pygame.Surface, elements: List[DrawContext]):
    surface.fill(WHITE)
    for element in elements:
        surface.blit(element.element, element.position)


def merge_surfaces(elements: List[DrawContext]) -> DrawContext:
    merged = pygame.Surface(DEFAULT_DIMENSION)
    merged.fill(WHITE)

    [merged.blit(element.element, (0, 0)) for element in elements]

    context = DrawContext(merged, (0, 0))
    context.is_valid = False

    return context

