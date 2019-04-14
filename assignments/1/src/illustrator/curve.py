from typing import List, Tuple

import pygame

from . import BaseIllustrator


class CurveIllustrator(BaseIllustrator):
    @staticmethod
    def compute_bezier_points(vertices, num_points=30):
        result = []

        b0x = vertices[0][0]
        b0y = vertices[0][1]
        b1x = vertices[1][0]
        b1y = vertices[1][1]
        b2x = vertices[2][0]
        b2y = vertices[2][1]
        b3x = vertices[3][0]
        b3y = vertices[3][1]

        # Compute polynomial coefficients from Bezier points
        ax = -b0x + 3 * b1x + -3 * b2x + b3x
        ay = -b0y + 3 * b1y + -3 * b2y + b3y

        bx = 3 * b0x + -6 * b1x + 3 * b2x
        by = 3 * b0y + -6 * b1y + 3 * b2y

        cx = -3 * b0x + 3 * b1x
        cy = -3 * b0y + 3 * b1y

        dx = b0x
        dy = b0y

        num_steps = num_points - 1
        h = 1.0 / num_steps

        point_x = dx
        point_y = dy

        first_fdx = ax * (h * h * h) + bx * (h * h) + cx * h
        first_fdy = ay * (h * h * h) + by * (h * h) + cy * h

        second_fdx = 6 * ax * (h * h * h) + 2 * bx * (h * h)
        second_fdy = 6 * ay * (h * h * h) + 2 * by * (h * h)

        third_fdx = 6 * ax * (h * h * h)
        third_fdy = 6 * ay * (h * h * h)

        result.append((int(point_x), int(point_y)))

        for i in range(num_steps):
            point_x += first_fdx
            point_y += first_fdy

            first_fdx += second_fdx
            first_fdy += second_fdy

            second_fdx += third_fdx
            second_fdy += third_fdy

            result.append((int(point_x), int(point_y)))

        return result

    def draw_bezier(self, control_points: List[Tuple]):
        b_points = CurveIllustrator.compute_bezier_points([x for x in control_points])
        pygame.draw.lines(self.gui_context.screen, self.options_context.line_color, False, b_points, 2)

        # Flip screen
        pygame.display.flip()

    def draw_line(self, *args, **kwargs):
        """
            User will first select 4 control points, then will change the
            accordingly. When its everything ok, will press 'ESC' to finish
            the curve and exit

        :param args: anything
        :param kwargs: anything
        """
        control_points = []
        original_position = kwargs.get('option_position')

        while len(control_points) < 4:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                is_pressed, _, __ = pygame.mouse.get_pressed()

                if is_pressed and mouse_position != original_position:
                    control_points.append(mouse_position)

        self.draw_bezier(control_points)

    def draw_circle(self, *args, **kwargs):
        print("Draw circle")
