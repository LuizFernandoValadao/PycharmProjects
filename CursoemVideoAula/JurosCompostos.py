n1 = float(input('Valor Inicial: '))
n2 = float(input('Valor Mensal: '))
m = int(input('Quantos meses: '))
t = float(input('Taxa(%): '))
r = n1
for i in range(1, m + 1):
    r = r * (1+t)
    r = r + n2

print('\033[34m-=-'*50)
print('\033[7;32;40mR${:.2f}\033[m'.format(r - n2))
