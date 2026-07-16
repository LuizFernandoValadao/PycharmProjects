lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if lista.count(5) == 0:
    print('o valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 faz parte da lista!')