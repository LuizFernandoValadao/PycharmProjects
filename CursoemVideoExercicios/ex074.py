from random import randint
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
valores = (n1, n2, n3, n4, n5)
print(f'Os valores sorteados foram: ', end='')
for c in valores:
    print(f'{c} ', end='')
valores_ordem = sorted(valores)
print(f'\nO maior valor sorteado foi {valores_ordem[-1]}')
print(f'O menor valor sorteado foi {valores_ordem[0]}')