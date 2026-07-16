nome = str(input('Qual é o seu nome? '))

cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',}

if nome == 'Gustavo':
    print('Que nome {}bonito{}!'.format(cores['vermelho'], cores['limpa']))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no {}Brasil{}.'.format(cores['verde'], cores['limpa']))
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome {}feminino{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('Seu nome é bem {}normal{}.'.format(cores['amarelo'], cores['limpa']))

print('Tenha um bom dia, {}{}{}!'.format(cores['azul'],nome,cores['limpa']))
