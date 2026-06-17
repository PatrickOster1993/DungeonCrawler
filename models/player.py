import pygame
from models.entity import Entity

class Player(Entity):

    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height, color, speed)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self._speed # speed = 5 Pixel pro Frame

        if keys[pygame.K_RIGHT]:
            self.rect.x += self._speed

        if keys[pygame.K_UP]:
            self.rect.y -= self._speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self._speed

    # Rechteck soll innerhalb eines anderen Rechtecks gehalten werden!
    def stay_in_bounds(self, screen_rect):
        self.rect.clamp_ip(screen_rect)