from main import app
from flask import render_template, request
#rotas

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template("registrar_contato.html")
    elif request.method == "POST":
        nome = request.form['nomeForm']
        telefone = request.form['telefoneForm']

        print(nome)
        print(telefone)

        return 'Usuario registrado'