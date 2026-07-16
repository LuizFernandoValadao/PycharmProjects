print('\033[1;31m↩️↪️'*15)
print('Sequência de Fibonacci')
print('\033[1m↩️↪️'*15)
n1 = 0
n2 = 1
r = int(input('➡➡➡\033[m Quantos elementos deseja mostrar? '))
c = 0
if r == 1:
    print(n1)
elif r == 2:
    print(n1, n2, sep=' ➡ ')
else:
    print(n1, n2, sep=' ➡ ', end=' ➡ ')
    while c < r - 2:
        n3 = n1 + n2
        print(n3, end=' ➡ ')
        n1 = n2
        n2 = n3
        c += 1
print('FIM')
#for c in range(0, r):
    #n3 = n1 + n2
    #print(n3, end=' -> ')
    #n1 = n2
    #n2 = n3