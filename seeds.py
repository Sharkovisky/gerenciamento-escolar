from app import db
from app.models.tables import Professor, Disciplina, Aluno
import bcrypt


# #Criando professores
# senha_plana = 'Suporte99' 
# senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
# p1 = Professor(nome='Marco Antônio 2', email='marco.andrade2@ifro.edu.br', senha=senha_encriptada)
# db.session.add(p1)
# db.session.commit()

# #Criando disciplinas
# d1 = Disciplina(nome='Banco de Dados', calculo='Soma')
# db.session.add(d1)
# db.session.commit()

# #Criando aluno
# senha_plana = 'alunorazao' 
# senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
# a1 = Aluno(nome='Nelson2', email='nelson.tremea2@gmail.com', senha=senha_encriptada)
# db.session.add(a1)
# db.session.commit()

# senha_plana = 'Suporte99' 
# senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
# p1 = Professor(nome='Roberto Guimaraes', email='roberto.guimaraes@ifro.edu.br', senha=senha_encriptada)
# db.session.add(p1)
# db.session.commit()

d1 = Disciplina(nome='Banco de Dados I', calculo='Soma')
d2 = Disciplina(nome='Banco de Dados II', calculo='Soma')
d3 = Disciplina(nome='Estrutura de Dados', calculo='Soma')
db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.commit()