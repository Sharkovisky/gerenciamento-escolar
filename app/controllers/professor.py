from app import app, db, login_manager
from flask import render_template, redirect, url_for, request
from flask_login import login_required
from app.models.tables import Professor
import bcrypt


@app.route('/professores')
@app.route('/professores/pagina/<int:pagina>/')
@login_required
def listar_professores(pagina=1):
    mensagem = request.args.get('msg')
    nome = request.args.get('nome')
    if nome:
        nome = '%' + nome + '%'
        lista = Professor.query.filter(Professor.nome.like(nome)).all()
    else:
        # lista = Professor.query.all()
        paginacao = Professor.query.paginate(page = pagina, per_page = 2)
        lista = paginacao.items
        total_paginas = paginacao.total

    return render_template("professor_listar.html", lista=lista, paginas=total_paginas, pagina_atual=pagina)


@app.route('/professores/deletar/<professor_id>')
def deletar_professor(professor_id):
    professor = Professor.query.filter_by(id=professor_id).first()
    db.session.delete(professor)
    db.session.commit()
    app.logger.info('O usuário Nelson deletou o professor '+professor_id)
    return redirect(url_for('listar_professores', msg='deletar'))

@app.route('/professores/alterar/<professor_id>', methods=['GET', 'POST'])
def alterar_professor(professor_id):
    if request.method == 'GET':
        professor = Professor.query.filter_by(id=professor_id).first()
        return render_template("professor_formulario.html", professor=professor, tipo='alterar')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        professor = Professor.query.filter_by(id=professor_id).first()
        professor.nome = nome
        professor.email = email

        db.session.add(professor)
        db.session.commit()

        return redirect(url_for('listar_professores', msg='alterar'))

@app.route('/professores/inserir', methods=['GET', 'POST'])
def inserir_professor():

    if request.method == 'GET':
        return render_template('professor_formulario.html', tipo='inserir')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        senha_plana = request.form['senha']
        senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())

        p1 = Professor(nome=nome, email=email, senha=senha_encriptada)
        db.session.add(p1)
        db.session.commit()
        return redirect(url_for('listar_professores', msg='inserir'))