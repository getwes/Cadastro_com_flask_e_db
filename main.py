from flask import Flask
from  db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db.init_app(app)

if __name__ == "__main__":
  
    from views import *
    app.run(debug=True)