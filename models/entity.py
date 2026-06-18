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

        # Sprite (also "Bild")
        self.__sprite = None

    @property
    def rect(self):
        return self._rect
    
    def draw(self, screen):

        if self.__sprite:
            screen.blit(
                self.__sprite,
                self.rect
            )
        else:
            pygame.draw.rect(
                surface=screen, # wohin wird gezeichnet?
                color=self.__color, # Farbe des Rechtecks!
                rect=self.rect
            )

    def load_sprite(self, image_path):
        raw_sprite = pygame.image.load(image_path).convert_alpha()
        self.__sprite = pygame.transform.smoothscale(raw_sprite, (self.rect.width, self.rect.height))

    @abstractmethod
    def update(self, context):
        pass