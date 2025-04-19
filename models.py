from db import db


class contato(db.Model):
    __tablename__ = 'contatos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)

    def __repr_(self):
        return f"<{self.nome}"