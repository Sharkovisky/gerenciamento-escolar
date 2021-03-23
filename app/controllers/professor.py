from app import app, db
from flask import render_template, redirect, url_for
from app.models.tables import Professor

@app.route('/professores')
def listar_professores():
    lista = Professor.query.all()
    return render_template("professor_listar.html", lista=lista)


@app.route('/professores/deletar/<professor_id>')
def deletar_professor(professor_id):
    professor = Professor.query.filter_by(id=professor_id).first()
    db.session.delete(professor)
    db.session.commit()
    return redirect(url_for('listar_professores', msg="deletar"))