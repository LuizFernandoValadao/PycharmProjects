matriz = [[0,0,0],[0,0,0],[0,0,0]]
totpares = terc = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            totpares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            terc += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {totpares}')
print(f'A soma dos valores da terceira coluna {terc}')
print(f'O maior valor da segunda linha {maior}')
