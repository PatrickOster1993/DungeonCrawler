from models.game_creature_data import GameCreatureData

class PokemonMapper:

    @staticmethod
    def map(pokemon_json):
        name = pokemon_json["key_bezeichnung_ähnlich_wie_name"]
        hp = pokemon_json["key_bezeichnung_ähnlich_wie_hp"]
        damage = pokemon_json["key_bezeichnung_ähnlich_wie_damage"]
        # vll. Sachen, die unklar mit eigener Logik
        # erweitern -> z. B. damage aus Kombination vieler stats / Attacen
        # Beispiel: Mittelwert aller Attacken-Damages = Variable "damage" in meinem Game!!!
        sprite = pokemon_json["key_bezeichnung_ähnlich_wie_sprite"]
        
        
        return GameCreatureData(
            name = name,
            hp = hp,
            damage = damage,
            sprite = sprite
        )