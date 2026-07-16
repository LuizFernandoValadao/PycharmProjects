
import random

aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno sorteado foi {}'.format(random.choice(lista)))