from app import app
from flask import render_template

@app.errorhandler(404)
def pagina_não_encontrada(e):
    return render_template("404.html"), 404