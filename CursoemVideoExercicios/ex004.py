#Verifica o que foi digitado

r = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(r)))
print('Só tem espaços? {}'.format(r.isspace()))
print('É um numero? {}'.format(r.isnumeric()))
print('É alfanumérico? {}'.format(r.isalnum()))
print('Está em maiusculas? {}'.format(r.isupper()))
print('Está em minusculas? {}'.format(r.islower()))
print('Está capitalizada? {}'.format(r.istitle()))
