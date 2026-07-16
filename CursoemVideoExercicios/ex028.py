import random
from time import sleep

n = random.randint(0, 5)
print('\033[1;33m-=-' * 20)
print('\033[1;34mVou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('\033[1;33m-=-\033[m' * 20)
r = int(input('Em que número eu pensei? '))
print('\033[1;34mPROCESSANDO...\033[m')
sleep(2)
print('PARABÉNS! Você conseguiu me vercer!' if r == n else 'GANHEI! Eu pensei no número {} e não no {}!'.format(n, r))
if r > 5:
    print('Digite um numero entre 0 e 5!')
