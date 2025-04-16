from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db = SQLAlchemy()
db.init_app(app)


class Usuario(db.Model):
  __tablename__ = 'usuarios'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(40), nullable=False, unique=True)

  def __repr__(self):
     return f"<{self.nome}>"


if __name__ == "__main__":
    with app.app_context():
        user = db.session.query(Usuario).filter_by(id=2).first()
        print(user)
    from views import *
    app.run(debug=True)