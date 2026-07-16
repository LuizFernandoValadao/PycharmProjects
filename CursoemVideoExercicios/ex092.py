from datetime import date
ano_atual = date.today().year
pessoas = dict()
pessoas['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoas['Idade'] = ano_atual - nasc
pessoas['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoas['CTPS'] != 0:
    pessoas['Ano de Contratacao'] = int(input('Ano de Contratação: '))
    pessoas['Salario'] = float(input('Sálario: R$'))
    if ano_atual - pessoas['Ano de Contratacao'] >= 35:
        pessoas['Aposentadoria'] = 'Pode Aposentar'
    else:
        pessoas['Aposentadoria'] = (pessoas['Ano de Contratacao'] + 35) - nasc
print('-='*30)
for k, v in pessoas.items():
    print(f'\033[1;34m{k}\033[m: {v}')

