n1 = int(input('Qual a tabuada você quer saber: '))
print('='*15)
for c in range(1, 11):
    print('{} x {:<2} = \033[1;32m{}\033[m'.format(c,n1, n1*c))
print('='*15)