from django.shortcuts import render, redirect
import requests
from random import randint
from django.contrib import messages

# Create your views here.


def index(request):
    try:
        pokemon = request.GET.get('id', '')
        if type(pokemon) is str:
            if pokemon == '':
                pokemon = randint(1, 905)
        if type(pokemon) is int:
            if int(pokemon) <= 0 or int(pokemon) >= 906:
                pokemon = 1

        info_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        info_pokemon = info_pokemon.json()

        info_pokemon_complementar = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}')
        info_pokemon_complementar = info_pokemon_complementar.json()

        numero_pokemon = info_pokemon['id']
        nome_pokemon = info_pokemon['name'].title()

        altura_pokemon_info = float(info_pokemon['height'])
        altura_pokemon = altura_pokemon_info / 10

        peso_pokemon_info = float(info_pokemon['weight'])
        peso_pokemon = peso_pokemon_info / 10

        tipo_pokemon = info_pokemon['types']
        lista_tipo_pokemon = []
        for tipo in tipo_pokemon:
            tipo_do_pokemon = tipo['type']['name'].title()
            lista_tipo_pokemon.append(tipo_do_pokemon)

        habilidades_pokemon = info_pokemon['abilities']
        lista_habilidades_pokemon = []
        for habilidade in habilidades_pokemon:
            if not habilidade['is_hidden']:
                nome_habilidade = habilidade['ability']['name'].title()
                lista_habilidades_pokemon.append(nome_habilidade)

        imagem_pokemon = info_pokemon['sprites']['other']['official-artwork']['front_default']

        cor_pokemon = info_pokemon_complementar['color']['name']

        if info_pokemon_complementar['is_baby']:
            raridade_pokemon = 'Baby'
        elif info_pokemon_complementar['is_legendary']:
            raridade_pokemon = 'Legendary'
        elif info_pokemon_complementar['is_mythical']:
            raridade_pokemon = 'Mythical'
        else:
            raridade_pokemon = 'Normal'

        lista_pokemon_stats = info_pokemon['stats']
        pokemon_stats = []
        for i in lista_pokemon_stats:
            stats = i['base_stat']
            pokemon_stats.append(stats)

        pokemon_display = {'id': numero_pokemon,
                           'nome': nome_pokemon,
                           'tipo': lista_tipo_pokemon,
                           'altura': altura_pokemon,
                           'peso': peso_pokemon,
                           'habilidade': lista_habilidades_pokemon,
                           'imagem': imagem_pokemon,
                           'cor': cor_pokemon,
                           'raridade': raridade_pokemon,
                           'estatistica': pokemon_stats}

        return render(request, 'pagina_inicial/base.html', pokemon_display)
    except:
        messages.error(request, f'Infelizmente esse Pokémon ainda não foi catalogado pelo time do Professor. Mas que tal esse outro aqui?!')
        return redirect('index')
