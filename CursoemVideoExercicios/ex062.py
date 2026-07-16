n = int(input('Digite um número: '))
n1 = n
pa = int(input('Digite a razão: '))
s = n + (10 * pa)
t = 0
while n < s:
    print('\033[1;34m{}'.format(n), end=' - ')
    n += pa
print('Pausa')
q = int(input('\n\033[1;33mQuantos termos deseja mostrar a mais? '))

while q != 0:
    s = n + (q * pa)
    while n < s:
        print('\033[1;34m{}'.format(n), end=' - ')
        n += pa
    t += q
    print('Pausa')
    q = int(input('\n\033[1;33mQuantos termos deseja mostrar a mais? '))
print('\033[1;32mProgressão finalizada com {} termos mostrados.'.format(t + 10))