from models.entity import Entity
from constants.game_settings import ENEMY_SIZE

class Enemy(Entity):
    def __init__(self, x, y, color, speed):
        super().__init__(
            x,
            y,
            ENEMY_SIZE,
            ENEMY_SIZE,
            color,
            speed
        )

        self.__hp = 100

        self.__observers = []
    
    def add_observer(self, observer):
        self.__observers.append(observer)

    def __notifiy_observers(self):
        for observer in self.__observers:
            observer.update(self.__hp)

    def update(self, context):
        self.rect.x -= self._speed

    @property
    def hp(self):
        return self.__hp
    
    def take_damage(self, damage):
        self.__hp -= damage
        self.__notifiy_observers()

    # gibt true zurück, wenn Enemy besiegt, weil ja 
    # dann self.__hp <= 0 "True" entspricht
    def is_dead(self):
        return self.__hp <= 0