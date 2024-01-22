import requests


def fetch_pokemon_data(pokemon_name):
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def check_if_in_red(pokemon_data):
    for game_index in pokemon_data['game_indices']:
        if game_index['version']['name'] == 'red':
            return True
    return False


def main():
    pokemon_name = 'ditto'  # Replace with the name of the Pokémon you want to check
    pokemon_data = fetch_pokemon_data(pokemon_name)

    if pokemon_data and check_if_in_red(pokemon_data):
        print(f"{pokemon_name.title()} appears in the Red version of the game.")
    else:
        print(f"{pokemon_name.title()} does not appear in the Red version of the game.")


if __name__ == "__main__":
    main()
