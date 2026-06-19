from models.creature import Creature
from constants.game_settings import ENEMY_SIZE

class Enemy(Creature):
    def __init__(self, x, y, color, speed, creature_data):
        super().__init__(
            x,
            y,
            ENEMY_SIZE,
            ENEMY_SIZE,
            speed,
            color,
            creature_data.hp
        )
        self.damage = creature_data.damage
        self.load_sprite(creature_data.sprite)

    def update(self, context):
        self.rect.x -= self._speed