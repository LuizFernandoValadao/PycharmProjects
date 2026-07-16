from time import sleep


def manual(h):
    a = (f" Acessando o manual do comando '{h}' ")
    print('\033[44m~'*len(a))
    print(a)
    print('~'*len(a))
    sleep(1)
    print('\033[7;37;40m', end='')
    help(h)
    sleep(1)


def titulo(t, c):
    if c == 1:
        print('\033[0;41m~' * len(t))
    if c == 2:
        print('\033[0;42m~' * len(t))
    if c == 4:
        print('\033[0;44m~' * len(t))
    print(t)
    print('~'*len(t))

while True:
    titulo(' SISTEMA DE AJUDA PyHELP ', 2)
    sleep(1)
    r = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
    if r == 'fim':
        break
    manual(r)
sleep(0.5)
titulo(' ATE LOGO! ', 1)