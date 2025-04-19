from db import db


class contato(db.model):
    __tablename__ = 'contatos'
    id = db.Column(db.Iteger, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullble=False)

    def __repr_(self):
        return f"<{self.nome}"