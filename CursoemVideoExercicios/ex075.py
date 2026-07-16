n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais número: '))
n4 = int(input('Digite o último número: '))
valores = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {(valores.index(3))+1}ª posicao')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for c in range(0, 4):
    if valores[c] % 2 == 0:
        print(valores[c], end=' ')
