from random import randint
from time import sleep
jogos = []
palpites = []
contador = 0
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, n):
    while True:
        s = randint(1, 60)
        if s not in palpites:
            palpites.append(s)
            contador += 1
        if contador >= 6:
            break
    contador = 0
    jogos.append(palpites[:])
    palpites.clear()
print(f'-=-=-=  SORTEANDO {n} JOGOS  -=-=-=')
for c, j in enumerate(jogos):
    sleep(1)
    print(f'Jogo {c+1}: {jogos[c]}')
print(f'{' < BOA SORTE! > ':=^40}')