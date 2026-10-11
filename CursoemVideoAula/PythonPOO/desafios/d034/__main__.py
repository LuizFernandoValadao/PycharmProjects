from classes import *
from rich import print, inspect

def main():
    f = Gerente('luiz', 1800)

    inspect(f, private=True, methods=True)
    print(f)

if __name__ == '__main__':
    main()