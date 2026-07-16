pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 18}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 87.6
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
