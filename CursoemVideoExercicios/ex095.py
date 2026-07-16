jogador = dict()
g = list()
j = list()
totg = 0
while True:
    print('-'*30)
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for c in range(0, partidas):
        g.append(int(input(f'Quantos gols na partida {c+1}? ')))
        totg += g[c]
    jogador['gols'] = g[:]
    jogador['total'] = totg
    g.clear()
    totg = 0
    j.append(jogador.copy())
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'cod {"nome":<17}{"gols":<16}total')
print('-'*50)
for c, jo in enumerate(j):
    print(f'{c:>3} ', end='')
    for i in jo.values():
        print(f'{str(i):<17}', end='')
    print()
while True:
    print('-'*50)
    dados = int(input('Mostrar dados de qual jogador? '))
    if dados == 999:
        break
    if dados >= len(j):
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {j[dados]["Nome"]}:')
        for i, g in enumerate(j[dados]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')