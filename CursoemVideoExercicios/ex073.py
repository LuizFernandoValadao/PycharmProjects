brasileirao = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR','Bragantino','Bahia', 'Coritiba', 'São Paulo',
              ' Atlético - MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 'EC Vitória', 'Internacional', 'Santos',
               'Grêmio', 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')
print('-='*15)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*15)
print(f'Os 5 primeiros colocados são: {brasileirao[:5]}')
print('-='*15)
print(f'Os 4 últimos colocados são: {brasileirao[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(brasileirao)}')
print('-='*15)
print(f'O Chapecoense está na {(brasileirao.index('Chapecoense'))+1}ª posição')