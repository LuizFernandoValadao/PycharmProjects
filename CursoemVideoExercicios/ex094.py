cadastro = dict()
pessoas = list()
toti = 0
media = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    toti += cadastro['idade']
    pessoas.append(cadastro.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'NS':
            break
        print('ERRO! Responda apenas S ou N:')
    if r == 'N':
        break
media = toti / len(pessoas)
print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print('\n- Lista das pessoas que estão acima da média:', end='')
for c in pessoas:
    if c['idade'] >= media:
        print('\n')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
print('\n<< ENCERRADO >>')
