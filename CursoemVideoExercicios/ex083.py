lista = str(input('Digite uma expressão: '))
if lista.index('(') < lista.index(')') and lista.count('(') == lista.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')