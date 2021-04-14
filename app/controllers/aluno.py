from app import app, db
from flask import render_template, redirect, url_for, request
from app.models.tables import Aluno

@app.route('/alunos')
@app.route('/alunos/pagina/<int:pagina>')
def listar_alunos(pagina=1):
    mensagem = request.args.get('msg')
    nome = request.args.get('nome')
    if nome:
        nome = '%'+ nome + '%'
        lista = Aluno.query.filter(Disciplina.nome.like(nome)).all()
    else:
        lista = Disciplina.query.all()
        # paginacao = Disciplina.query.paginate(page=pagina, per_page=5)
        # lista = paginacao.items
        # total_paginas = paginacao.total

    return render_template("alunos_listar.html", lista=lista, total_paginas=total_paginas, pagina_atual=pagina)

@app.route('/alunos/deletar/<aluno_id>')
def deletar_aluno(aluno_id):
    aluno = Aluno.query.filter_by(id=aluno_id).first()
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('listar_alunos', msg='deletar'))

@app.route('/alunos/alterar/<disciplina_id>)', methods=['GET', 'POST'])
def alterar_aluno(aluno_id):
    if request.method == 'GET':
        aluno = Disciplina.query.filter_by(id=aluno_id).first()
        return render_template("aluno_formulario.html", aluno=aluno, tipo='alterar')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        aluno = Aluno.query.filter_by(id=aluno_id).first()
        aluno.nome = nome
        aluno.email = email

        db.session.add(aluno)
        db.session.commit()

        return redirect(url_for('listar_alunos', msg='alterar'))

@app.route('/alunos/inserir', methods=['GET', 'POST'])
def inserir_aluno():
    if request.method == 'GET':
        return render_template('aluno_formulario.html', tipo='inserir')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        d1 = Aluno(nome=nome, email=email)
        db.session.add(d1)
        db.session.commit()
        return redirect(url_for('listar_alunos', msg='inserir'))