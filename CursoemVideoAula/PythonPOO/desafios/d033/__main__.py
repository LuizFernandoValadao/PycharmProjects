from rich import print, inspect
from classd033 import *

def main():
    a = Aluno('Marcia', 2010, "ADM")
    b = Aluno('Pedro', 2015, "ENG")

    a.add_curso("MODA")

    inspect(a, private=True, methods=True)


if __name__ == '__main__':
    main()