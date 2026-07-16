from random import randint
from time import sleep

pc = randint(0,10)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 10')
print('-=-'*20)
numero = int(input('Digite um numero entre 0 e 10: '))
chances = 0
while numero != pc:
    chances += 1
    if numero > pc:
        numero = int(input('Menos... Tente mais uma vez: '))
    elif numero < pc:
        numero = int(input('Mais... Tente mais uma vez: '))
print('PROCESSANDO...')
sleep(2)
print('PARABENS! Voce acertou!')
print('Foi necessario {} chances'.format(chances + 1))