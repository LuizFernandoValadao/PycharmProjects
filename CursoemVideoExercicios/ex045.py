import random

print('\033[32m-=-'*15)
print('\033[1;31m          J - O - K - E - N - P - O')
print('\033[32m-=-'*15)
print('\033[m| 1 - \033[1;37mPEDRA')
print('\033[m| 2 - \033[1;36mPAPEL')
print('\033[m| 3 - \033[1;33mTESOURA')
print('\033[32m-=-'*15)
jogador = str(input('\033[1;34mEscolha sua jogada: ')).strip().upper()
print('\033[32m-=-'*15)

if jogador == '1':
    jogador = 'PEDRA'
elif jogador == '2':
    jogador = 'PAPEL'
elif jogador == '3':
    jogador = 'TESOURA'

pc = random.randint(1, 3)
if pc == 1:
    pc = 'PEDRA'
elif pc == 2:
    pc = 'PAPEL'
elif pc == 3:
    pc = 'TESOURA'

print('\033[1;34mJogador: {}'.format(jogador))
print('\033[1;31mComputador: {}'.format(pc))
print('\033[32m-=-\033[1;33m'*15)

if jogador == pc:
    print('EMPATE!')
elif jogador == 'PEDRA' and pc == 'TESOURA':
    print('Jogador venceu!')
elif jogador == 'PEDRA' and pc == 'PAPEL':
    print('Computador venceu!')
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print('Jogador venceu!')
elif jogador == 'TESOURA' and pc == 'PEDRA':
    print('Computador venceu!')
elif jogador == 'PAPEL' and pc == 'PEDRA':
    print('Jogador venceu!')
elif jogador == 'PAPEL' and pc == 'TESOURA':
    print('Computador venceu!')
