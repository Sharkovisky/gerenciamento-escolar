from app import db
from flask_login import UserMixin

class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), index=True, unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome

    def __repr__(self):
        return '<Professor %s>' % self.nome

class Disciplina(db.Model):
    __tablename__ = 'disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    calculo = db.Column(db.String(20), nullable=False, default="Soma")

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome

    def __repr__(self):
        return '<Disciplina %s>' % self.nome

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), index=True, unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Aluno %s>' % self.nome

class ProfessorDisciplina(db.Model):
    __tablename__ = 'professores_disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)

    def __repr__(self):
        return '<Disciplinas do professor %d>' % self.professor_id

class Etapa(db.Model):
    __tablename__ = 'etapas'

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)
    descricao = db.Column(db.String(200), index=True, nullable=False)

    def __repr__(self):
        return '<Etapa %s>' % self.descricao

class Nota(db.Model):
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    etapa_id = db.Column(db.Integer, db.ForeignKey('etapas.id'), nullable=False)
    nota = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Nota %f da etapa %d>' % self.nota, self.etapa_id