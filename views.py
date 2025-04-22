from main import app
from flask import render_template, request
from models import contato
from db import db
#rotas

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET'
        return render_template("registrar_contato.html")