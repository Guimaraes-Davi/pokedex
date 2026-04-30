from flask import Flask, jsonify
from app.pokeapi import buscar_pokemon

app = Flask(__name__)

@app.route("/pokemon/<nome>")
def get_pokemon(nome):
    pokemon = buscar_pokemon(nome)

    if pokemon:
        return jsonify(pokemon)
    else:
        return jsonify({"erro": "Pokémon não encontrado"}), 404