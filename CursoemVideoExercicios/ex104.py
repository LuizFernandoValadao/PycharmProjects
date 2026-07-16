def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabor de digitar o número {n}')