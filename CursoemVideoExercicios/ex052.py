n = int(input('Digite um número: '))
primo = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end=' ')
        primo += 1
    else:
        print('\033[31m', end=' ')

    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, primo))
if primo == 2:
    print('\033[1;32mE por isso ele é PRIMO!')
elif primo > 2:
    print('\033[1;31mE por isso ele não é PRIMO!')
