n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
r = int(input('Escolha uma opção: '))
if r == 1:
    print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
elif r == 2:
    print('O produto entre {} e {} é {:.2f}'.format(n1, n2, n1*n2))
elif r == 3:
    if n1 > n2:
        print('O maior número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n2))
elif r == 4:
    continuar = 'S'
    while continuar == 'S':
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
        r = int(input('Escolha uma opção: '))
        if r == 1:
            print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        elif r == 2:
            print('O produto entre {} e {} é {}'.format(n1, n2, n1 * n2))
        elif r == 3:
            if n1 > n2:
                print('O maior número é {}'.format(n1))
            else:
                print('O maior número é {}'.format(n2))
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
