from app import app, db
from flask import render_template, redirect, url_for, request
from app.models.tables import Disciplina

@app.route('/disciplinas')
def listar_disciplinas():
    mensagem = request.args.get('msg')
    nome = request.args.get('nome')
    if nome:
        nome = '%'+ nome + '%'
        lista = Disciplina.query.filter(Disciplina.nome.like(nome)).all()
    else:
        lista = Disciplina.query.all()

    return render_template("disciplina_listar.html", lista=lista)