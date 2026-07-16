cont = 0
soma = 0
while True:
    n = int(input('Digite um valor \033[1;31m(999 para parar)\033[m: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'\033[1;34mA soma dos {cont} valores foi {soma}!')