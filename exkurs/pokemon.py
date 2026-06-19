import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=3")
data = response.json()
results = data["results"]

pokemon = []
for result in results:
    response_pokemon = requests.get(result["url"])
    data_pokemon = response_pokemon.json()
    pokemon.append(data_pokemon)

print(pokemon[0])