tot = 0
soma = 0
n1 = int(input('Digite um número [999 para parar]: '))
while n1 != 999:
    soma += n1
    tot += 1
    n1 = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma deles é {}'.format(tot,soma))
