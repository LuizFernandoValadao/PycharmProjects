from termostato import*
from rich import print, inspect

def main():
    try:
        t = Termostato()
        t.temperatura = 16.5
    except Exception as e:
        print(f'Houve um problema: {e}')

    print(f'A temperatura atual é {t.ftemperatura}')

if __name__ == '__main__':
    main()