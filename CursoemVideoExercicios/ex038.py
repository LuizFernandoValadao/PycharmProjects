n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('\033[1;31m-=-' * 9)
    print('\033[33m-\033[m O \033[33mprimeiro valor\033[m é \033[34mmaior\033[m!')
elif n1 < n2:
    print('\033[1;31m-=-' * 9)
    print('\033[33m-\033[m O \033[33msegundo valor\033[m é \033[34mmaior\033[m!')
else:
    print('\033[1;31m-=-' * 15)
    print('\033[33m- Não existe \033[mvalor maior, os dois são \033[34miguais\033[m!')
