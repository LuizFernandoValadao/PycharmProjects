from classes import *
from rich import print, inspect

def main():
    f = Designer('Ana', 12000)
    f.salario = 15000

    inspect(f, private=True, methods=True)
    print(f)

if __name__ == '__main__':
    main()