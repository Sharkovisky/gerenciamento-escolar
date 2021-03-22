from app import db
from app.models.tables import Professor, Disciplina, Aluno
import bcrypt


#Criando professores
senha_plana = 'Suporte99' 
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
p1 = Professor(nome='Marco Antônio', email='marco.andrade@ifro.edu.br', senha=senha_encriptada)
db.session.add(p1)
db.session.commit()

#Criando disciplinas
d1 = Disciplina(nome='Banco de Dados', calculo='60 de prova e 40 de trabalhos')
db.session.add(d1)
db.session.commit()

#Criando aluno
senha_plana = 'alunorazao' 
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
a1 = Aluno(nome='Nelson', email='nelson.tremea@gmail.com', senha=senha_encriptada)
db.session.add(a1)
db.session.commit()