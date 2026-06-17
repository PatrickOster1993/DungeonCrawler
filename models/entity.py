import pygame

class Entity:

    def __init__(self, x, y, width, height, color, speed):

        # Position
        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        # Geschwindigkeit
        self._speed = speed

        # Farbe
        self.__color = color


    def draw(self, screen):
        pygame.draw.rect(
            surface=screen, # wohin wird gezeichnet?
            color=self.__color, # Farbe des Rechtecks!
            rect=self.rect
        )