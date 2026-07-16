from time import sleep


def maior(*valores):
    m = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for c, num in enumerate(valores):
        sleep(0.3)
        print(f'{num} ', end='')
        if c == 0:
            m = num
        else:
            if num > m:
                m = num
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()