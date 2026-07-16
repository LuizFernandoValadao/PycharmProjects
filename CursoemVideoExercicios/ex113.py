from time import sleep


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[33mEntrada de dados interrompida pelo usúario.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[33mEntrada de dados interrompida pelo usúario.\033[m')
            return 0
        else:
            return n


numint = leiaInt('Digite um valor inteiro: ')
numfloat = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {numint}')
print(f'O valor real digitado foi {numfloat}')
print(f'Falta (', end='', flush=True)
for n in range(5, 0, -1):
    sleep(1)
    print(n, end=' ', flush=True)