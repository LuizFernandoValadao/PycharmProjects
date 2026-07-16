n = int(input('Digite um número: '))
par = impar = 0
while n != 0:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    n = int(input('Digite um número: '))
print('No total você digitou {} números pares\nNo total você digitou {} números impares'.format(par, impar))