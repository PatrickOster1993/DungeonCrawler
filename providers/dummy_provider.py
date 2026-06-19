from providers.game_data_provider import GameDataProvider
from models.game_creature_data import GameCreatureData
import json

class DummyProvider(GameDataProvider):
    def load_creatures(self):
        # muss danach implementiert werden!
        with open(
            "data/dungeon.json",
            "r"
        ) as file:
            dungeon_data = json.load(file)
            creatures = []

            for enemy_data in dungeon_data["enemies"]:
                creatures.append(
                    GameCreatureData(
                        name=enemy_data["name"],
                        hp=enemy_data["hp"],
                        damage=enemy_data["damage"],
                        sprite=enemy_data["sprite"]
                    )
                )
            return creatures




        # return [
        #     GameCreatureData(
        #         name="Elf",
        #         hp=50,
        #         damage=5,
        #         sprite=None
        #     ),
        #     GameCreatureData(
        #         name="Goblin",
        #         hp=100,
        #         damage=10,
        #         sprite=None
        #     )
        # ]
    
