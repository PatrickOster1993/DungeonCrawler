from models.entity import Entity

class Creature(Entity):
    
    def __init__(self, x, y, width, height, speed, color, hp):
        super().__init__(
            x, y, width, height, color
        )

        self.__hp = hp

        self.__observers = []

        self._speed = speed

        # Rechteck soll innerhalb eines anderen Rechtecks gehalten werden!
    def stay_in_bounds(self, screen_rect):
        self.rect.clamp_ip(screen_rect)

    @property
    def hp(self):
        return self.__hp
    
    def take_damage(self, damage):
        self.__hp -= damage
        self.__notifiy_observers()

    def is_dead(self):
        return self.__hp <= 0
    
    def add_observer(self, observer):
        self.__observers.append(observer)

    def __notifiy_observers(self):
        for observer in self.__observers:
            observer.update(self.__hp)