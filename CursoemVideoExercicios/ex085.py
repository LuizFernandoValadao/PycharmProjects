valores = [[],[]]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print('-='*30)
print(f'Os valores os pares digitados foram: {valores[0]}')
print(f'Os valores impares digitados foram: {valores[1]}')
