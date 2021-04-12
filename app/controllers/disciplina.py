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

@app.route('/disciplinas/deletar/<disciplina_id>')
def deletar_disciplina(disciplina_id):
    disciplina = Disciplina.query.filter_by(id=disciplina_id).first()
    db.session.delete(disciplina)
    db.session.commit()
    return redirect(url_for('listar_disciplinas', msg='deletar'))

@app.route('/disciplinas/alterar/<disciplina_id>)', methods=['GET', 'POST'])
def alterar_disciplina(disciplina_id):
    if request.method == 'GET':
        disciplina = Disciplina.query.filter_by(id=disciplina_id).first()
        return render_template("disciplina_formulario.html", disciplina=disciplina, tipo='alterar')
    elif request.method == 'POST':
        nome = request.form['nome']
        calculo = request.form['calculo']

        disciplina = Disciplina.query.filter_by(id=disciplina_id).first()
        disciplina.nome = nome
        disciplina.calculo = calculo

        db.session.add(disciplina)
        db.session.commit()

        return redirect(url_for('listar_disciplinas', msg='alterar'))

@app.route('/disciplinas/inserir', methods=['GET', 'POST'])
def inserir_disciplina():
    if request.method == 'GET':
        return render_template('disciplina_formulario.html', tipo='inserir')
    elif request.method == 'POST':
        nome = request.form['nome']
        calculo = request.form['calculo']

        d1 = Disciplina(nome=nome, calculo=calculo)
        db.session.add(d1)
        db.session.commit()
        return redirect(url_for('listar_disciplinas', msg='inserir'))