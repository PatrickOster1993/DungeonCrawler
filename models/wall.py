import pygame
from constants.colors import Colors
from models.entity import Entity


class Wall(Entity):

    def __init__(
        self,
        x,
        y,
        width,
        height
    ):

        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            color=Colors.WHITE.value
        )

    def update(self, context):
        pass