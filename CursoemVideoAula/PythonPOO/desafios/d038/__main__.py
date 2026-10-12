from classes import *
from rich import print, inspect

def main():
    p1 = Produto('Notebook', 8500)
    p2 = Produto('Mouse', 250)
    p3 = Produto('Fone de Ouvido', 450.35)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p2 + p3
    c2 = c2 + c1 + p1

    print(f'\nCARRINHO 1',c1)
    print(f'\nCARRINHO 2',c2)


if __name__ == '__main__':
    main()