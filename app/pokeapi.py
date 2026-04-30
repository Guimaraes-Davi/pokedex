import requests

def buscar_pokemon(nome):
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