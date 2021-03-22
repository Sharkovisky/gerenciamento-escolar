from app import app
from flask import render_template

@app.route('/alunos')
def listar_alunos():
    return '<h1>Listando alunos</h1>'