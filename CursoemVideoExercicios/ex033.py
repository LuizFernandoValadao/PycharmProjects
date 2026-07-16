n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print('O \033[31mmaior\033[m numero é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O \033[31mmaior\033[m numero é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O \033[31mmaior\033[m numero é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O \033[34mmenor\033[m numero é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O \033[34mmenor\033[m numero é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O \033[34mmenor\033[m numero é {}'.format(n3))
