brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
for i in brasil:
    for k, v in i.items():
        print(f'{k}: {v}')
    print('-='*20)

