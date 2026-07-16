from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f or p < 0:
        for c in range(i, f-1, -p):
            sleep(0.3)
            print(f'{c}', end=' ')
        print('FIM!')
    else:
        for c in range(i, f+1, p):
            sleep(0.3)
            print(f'{c}', end=' ')
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)