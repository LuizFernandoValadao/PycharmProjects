n = int(input('Digite um número: '))
pa = int(input('Digite a razão: '))
s = n + (10 * pa)
for c in range(n, s, pa):
    print('\033[1;34m',c, end=' -')
print(' Acabou')
