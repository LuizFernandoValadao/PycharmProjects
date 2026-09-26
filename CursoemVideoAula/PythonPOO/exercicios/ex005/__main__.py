from rich import print
from rich import inspect
from classesex005 import *


a1 = Aluno('José', 17, 'Informática', 'T01')
a1.fazer_matricula()
a1.fazer_aniversario()
inspect(a1)


p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario('Claudia', 27, 'Secretária', 'Secretaria')
f1.fazer_aniversario()
f1.bater_pontos()
inspect(f1, methods=True)

