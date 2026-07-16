from random import randint
pc = randint(1, 10)
soma = 0
resp = ''
cont = 0
print('-=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*20)
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    soma = n + pc
    if r == 'P':
        r = 'PAR'
    elif r == 'I':
        r = 'IMPAR'

    if soma % 2 == 0:
        resp = 'PAR'
    elif soma % 2 == 1:
        resp = 'IMPAR'

    print('-'*40)
    print(f'Você jogou {n} e o computador {pc}. Total de {soma} deu {resp}')
    print('-' * 40)
    if resp == r:
        print('Você Venceu!\nVamos jogar novamente...')
        print('-=' * 20)
        cont += 1
    else:
        break
print('Você PERDEU!')
print('-=' * 20)
print(f'GAME OVER! Você venceu {cont} vezes.')
