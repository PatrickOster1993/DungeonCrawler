from models.creature import Creature
from constants.game_settings import ENEMY_SIZE

class Enemy(Creature):
    def __init__(self, x, y, color, speed):
        super().__init__(
            x,
            y,
            ENEMY_SIZE,
            ENEMY_SIZE,
            speed,
            color,
            hp=100
        )

    def update(self, context):
        self.rect.x -= self._speed