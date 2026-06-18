import pygame
from models.creature import Creature

class Player(Creature):

    def __init__(self, x, y, width, height, color, speed, hp):
        super().__init__(x, y, width, height, speed, color, hp)

    def __move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self._speed # speed = 5 Pixel pro Frame

        if keys[pygame.K_RIGHT]:
            self.rect.x += self._speed

        if keys[pygame.K_UP]:
            self.rect.y -= self._speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self._speed

    def update(self, context):
        self.__move(context)

