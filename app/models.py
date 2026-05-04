from app.database import db

class Favorito(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    pokemon_id = db.Column(db.Integer, nullable=False)
    tipos = db.Column(db.String(100), nullable=False)
    imagem = db.Column(db.String(300),  nullable=False)

