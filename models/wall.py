import pygame
from constants.colors import Colors

class Wall:

    def __init__(self, x, y, width, height):

        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            Colors.WHITE.value,
            self.rect
        )