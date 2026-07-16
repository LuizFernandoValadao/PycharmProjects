print('Gerador de PA')
print('-='*10)
n = int(input('Primeiro termo: '))
pa = int(input('Razão da PA: '))
s = n + (10 * pa)
while n < s:
    print('\033[1;34m{}'.format(n), end=' ➡ ')
    n += pa
print('Fim')