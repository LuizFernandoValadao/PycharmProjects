lista1 = list()
lista2 = list()
lista3 = list()
while True:
    n = int(input('Digite um número: '))
    lista1.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for l in lista1:
    if l % 2 == 0:
        lista2.append(l)
    else:
        lista3.append(l)
print('-='*30)
print(f'A lista completa é {lista1}')
print(f'A lista de pares é {lista2}')
print(f'A lista de impares é {lista3}')