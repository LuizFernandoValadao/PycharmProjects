def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero
    :param n: O número a ser calculado
    :param show: (opicional) Mostrar ou não a conta
    :return: O valor do fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' =', end=' ')
    print(f'{f} ')

print('-'*30)
fatorial(5, show=False)
