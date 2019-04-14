from . import BaseIllustrator


class SquareIllustrator(BaseIllustrator):
    def draw_line(self, *args, **kwargs):
        print('Draw single line')

    def draw_circle(self, *args, **kwargs):
        print("Draw circle")