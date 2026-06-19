from providers.game_data_provider import GameDataProvider
from mappers.pokemon_mapper import PokemonMapper

class PokemonProvider(GameDataProvider):
    def load_creatures(self):
        # muss danach implementiert werden!
        
        # API Aufruf (Roh-JSON-Daten grob aufbereitet für Mapper!)
        # dann erhalten wir eine Liste an pokemon für die wir machen:
        pokemons = [] # = Liste aus Dict-Daten
        creatures = []
        for pokemon in pokemons:
            creatures.append(PokemonMapper.map(pokemon))
        
        return creatures