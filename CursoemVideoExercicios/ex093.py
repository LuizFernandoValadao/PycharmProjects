jogador = dict()
g = list()
totg = 0
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for c in range(0, partidas):
    g.append(int(input(f'Quantos gols na partida {c}? ')))
    totg += g[c]
jogador['gols'] = g[:]
jogador['total'] = totg
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for i, c in enumerate(g):
    print(f'    => Na partida {i}, fez {c} gols')
print(f'Foi um total de {totg} gols.')
