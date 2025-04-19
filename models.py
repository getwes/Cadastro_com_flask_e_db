from db import db

class contato(db.model):
    __tablename__ = 'contatos'

    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullble=False)