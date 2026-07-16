n = int(input('Digite um número para\ncalcular seu fatorial: '))
s = n
print('Calculando {}! = {}'.format(s, s), end= '')
while n > 1:
    n -= 1
    s = s * n
    print(' x {}'.format(n), end= '')
print(' = \033[1;34m{}'.format(s))
