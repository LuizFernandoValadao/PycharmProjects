from time import sleep
from random import randint
números = list()


def sorteia():
    print('Sorteando 5 valores de lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        sleep(0.3)
        print(f'{n} ', end='')
        números.append(n)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {números}, temos {soma}')


sorteia()
somaPar(números)