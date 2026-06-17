import pygame

class Player:

    def __init__(self):

        # Position
        self.rect = pygame.Rect(
            100,
            100,
            50,
            50
        )

        # Geschwindigkeit
        self.__speed = 5

    def draw(self, screen):
        pygame.draw.rect(
            surface=screen, # wohin wird gezeichnet?
            color=(0, 255, 0), # Farbe des Rechtecks!
            rect=self.rect
        )

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.__speed # speed = 5 Pixel pro Frame

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.__speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.__speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.__speed

    # Rechteck soll innerhalb eines anderen Rechtecks gehalten werden!
    def stay_in_bounds(self, screen_rect):
        self.rect.clamp_ip(screen_rect)