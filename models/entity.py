import pygame
from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self, x, y, width, height, color, speed):

        # Position
        self._rect = pygame.Rect(
            x,
            y,
            width,
            height
        )
        
        # Geschwindigkeit
        self._speed = speed

        # Farbe
        self.__color = color

    @property
    def rect(self):
        return self._rect
    
    def draw(self, screen):
        pygame.draw.rect(
            surface=screen, # wohin wird gezeichnet?
            color=self.__color, # Farbe des Rechtecks!
            rect=self.rect
        )

    @abstractmethod
    def update(self, context):
        pass