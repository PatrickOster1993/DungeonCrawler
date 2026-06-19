from abc import ABC, abstractmethod

# Interface!!!
class GameDataProvider(ABC):

    @abstractmethod
    def load_creatures(self):
        pass