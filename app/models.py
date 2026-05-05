from app.database import db

class Favorito(db.Model):
    """
    Modelo que representa um pokémon salvo como favorito.

    Attributes:
        id (int): Identificador único gerado automaticamente.
        nome (str): Nome do pokémon.
        pokemon_id (int): ID do pokémon na PokeAPI.
        tipos (str): Tipos do pokémon separados por vírgula.
        imagem (str): URL da imagem oficial do pokémon.
    """
    id = db.Column(db.Integer,  primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    pokemon_id = db.Column(db.Integer, nullable=False)
    tipos = db.Column(db.String(100), nullable=False)
    imagem = db.Column(db.String(300),  nullable=False)

