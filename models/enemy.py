from models.entity import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            50,
            50,
            (255,0,0),
            2
        )
