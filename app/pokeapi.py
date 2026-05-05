import requests

def buscar_pokemon(nome):
    """
    Busca os dados de um pokémon pelo nome na PokeAPI.

    Args:
        nome (str): Nome do pokémon a ser buscado.

    Returns:
        dict: Dicionário com nome, id, altura, peso, tipos, stats e imagem.
        None: Se o pokémon não for encontrado.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        pokemon = {
            "nome": dados["name"],
            "id": dados["id"],
            "altura": dados["height"],
            "peso": dados["weight"],
            "tipos": [t["type"]["name"] for t in dados["types"]],
            "stats": {s["stat"]["name"]: s["base_stat"] for s in dados["stats"]},
            "imagem": dados["sprites"]["other"]["official-artwork"]["front_default"]
        }

        return pokemon
    else:
        return None