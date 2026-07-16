from time import sleep
alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-=' * 30)
print(f'{'No.':3} {'NOME':18}MÉDIA')
print('-'*30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:20}{a[2]:.1f}')
while True:
    print('-' * 40)
    r = int(input('Mostrar notas de qual aluno? (999 interrompa) '))
    for i, a in enumerate(alunos):
        if i == r:
            print(f'Notas de {a[0]} são {a[1]}')
    if r == 999:
        print('Finalizando...')
        sleep(2)
        break
print('<<< VOLTE SEMPRE! >>>')

