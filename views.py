from main import app
from flask import render_template, request, redirect, url_for
from models import Contato
from  db import db
#rotas

@app.route("/")
def homepage():
    contatos = db.session.query(Contato).all()
    return render_template("homepage.html", contatos=contatos)

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template("registrar_contato.html")
    elif request.method == "POST":
        nome = request.form['nomeForm']
        telefone = request.form['telefoneForm']

        novo_contato = Contato(nome=nome, telefone=telefone)
        db.session.add(novo_contato)
        db.session.commit()


        return redirect(url_for('homepage'))