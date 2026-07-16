n1 = int(input('Digite um numero inteiro: '))
if n1 % 2 == 0:
    print('O número {} é \033[1;34mPar'.format(n1))
else:
    print('O número {} é \033[1;31mImpar'.format(n1))