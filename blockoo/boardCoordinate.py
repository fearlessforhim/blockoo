from .color import Color


class BoardCoordinate:

    def __init__(self, color):
        self.color = color

    def asJson(self):
        return {'color': self.color.value}