import pygame
from observers.observer import Observer
from constants.colors import Colors

class HUD(Observer):
    def __init__(self):
        
        self.__font = pygame.font.Font(
            None,
            36
        )

        self.__enemy_hp = 0
    
    def update(self, hp):
        self.__enemy_hp = hp

    def set_enemy_hp(self, hp):
        self.__enemy_hp = hp

    def draw(self, screen):

        text = self.__font.render(
            f"Enemy HP: {self.__enemy_hp}",
            True,
            Colors.WHITE.value
        )

        screen.blit(
            text,
            (10, 10)
        )
