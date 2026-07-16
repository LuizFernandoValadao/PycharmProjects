n1 = int(input('Digite um número inteiro: '))
print('\033[31m-'*20)
print('\033[33m-\033[34m 1\033[m para \033[33mBinario\033[m')
print('\033[33m-\033[34m 2\033[m para \033[33mOctal')
print('\033[33m-\033[34m 3\033[m para \033[33mHexadecimal')
print('\033[31m-\033[m'*20)
base = int(input('Escolha a base de conversão:'))
if base == 1:
    print('{} em binario fica {}!'.format(n1, bin(n1)[2:]))
elif base == 2:
    print('{} em octal fica {}!'.format(n1, oct(n1)[2:]))
elif base == 3:
    print('{} em hexadecimal fica {}!'.format(n1, hex(n1)[2:]))
else:
    print('\033[1;31mESCOLHA UM NUMERO DE 1 A 3 PARA SELECIONAR A BASE!')