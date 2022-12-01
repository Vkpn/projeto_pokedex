import requests

pokemon = str(input(f'Digite o nome ou o numero do pokemon: '))
info_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
info_pokemon = info_pokemon.json()
for i in info_pokemon.items():
    print(i)
print('--' * 20)
for i in info_pokemon['stats']:
    print(i['base_stat'])


