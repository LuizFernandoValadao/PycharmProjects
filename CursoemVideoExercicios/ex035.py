r1 = float(input('Digite o comprimento da 1º reta: '))
r2 = float(input('Digite o comprimento da 2º reta: '))
r3 = float(input('Digite o comprimento da 3º reta: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('\033[1;32mÉ um triangulo!')
else:
    print('\033[1;31mNão dá para formar um triangulo!')