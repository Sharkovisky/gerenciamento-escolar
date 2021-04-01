from app import app, db, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app.models.tables import Professor
import bcrypt

@login_manager.user_loader
def get_user(user_id):
    return Professor.query.filter_by(id=user_id).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        mensagem = request.args.get('mensagem')
        return render_template("login.html")
    elif request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        professor = Professor.query.filter_by(email=email).first()
        autorizado = False

        if professor:
            autorizado = bcrypt.checkpw(senha.encode('utf-8'), professor.senha.encode('utf-8'))

        if not professor or not autorizado:
            mensagem = "Login não autorizado"
            return render_template('login.html', mensagem=mensagem)
        else:
            login_user(professor)
            return redirect('/professores')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@login_manager.unauthorized_handler
def nao_autorizado():
    return redirect(url_for('login', mensagem='Faça login para acessar este recurso'))