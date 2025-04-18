from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == "__main__":
  
    from views import *
    app.run(debug=True)