r1 = float(input('Digite o comprimento da 1º reta: '))
r2 = float(input('Digite o comprimento da 2º reta: '))
r3 = float(input('Digite o comprimento da 3º reta: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('\033[1;32mÉ um triangulo!')
    if r1 == r2 == r3:
        print('\033[1;33m- \033[1;34mEquilatero\033[m: todos os lados iguais\n'
              '\033[1;33m- \033[1;34mIsósceles\033[m: dois lados iguais')
    elif r1 != r2 != r3 != r1:
        print('\033[1;33m- \033[1;34mEscaleno\033[m: todos os lados diferentes')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('\033[1;33m- \033[1;34mIsósceles\033[m: dois lados iguais')
else:
    print('\033[1;31mNão dá para formar um triangulo!')