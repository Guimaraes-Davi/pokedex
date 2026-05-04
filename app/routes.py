from flask import Flask, jsonify, request
from app.database import db
from app.pokeapi import buscar_pokemon
from app.models import Favorito
from flask import render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokedex.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/pokemon/<nome>")
def get_pokemon(nome):
    pokemon = buscar_pokemon(nome)
    if pokemon:
        return jsonify(pokemon)
    return jsonify({"erro": "Pokémon não encontrado"}), 404

@app.route("/favoritos", methods=["POST"])
def adicionar_favorito():
    dados = request.get_json()
    novo = Favorito(
        nome=dados["nome"],
        pokemon_id=dados["id"],
        tipos=", ".join(dados["tipos"]),
        imagem=dados["imagem"]
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": f"{dados['nome']} adicionado aos favoritos!"}), 201

@app.route("/favoritos", methods=["GET"])
def listar_favoritos():
    favoritos = Favorito.query.all()
    resultado = [
        {
            "id": f.id,
            "nome": f.nome,
            "pokemon_id": f.pokemon_id,
            "tipos": f.tipos,
            "imagem": f.imagem
        }
        for f in favoritos
    ]
    return jsonify(resultado)

@app.route("/favoritos/<int:id>", methods=["DELETE"])
def remover_favorito(id):
    favorito = Favorito.query.get(id)
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({"mensagem": f"{favorito.nome} removido dos favoritos!"})
    return jsonify({"erro": "Favorito não encontrado"}), 404

@app.route("/")
def index():
    return render_template("index.html")