while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = \033[1;32m{n*c}\033[m')
    print('-'*40)
print('FIM')
print('-'*40)
