from models.entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, color, speed):
        super().__init__(
            x,
            y,
            50,
            50,
            color,
            speed
        )
    
    def update(self, context):
        self.rect.x -= self._speed
