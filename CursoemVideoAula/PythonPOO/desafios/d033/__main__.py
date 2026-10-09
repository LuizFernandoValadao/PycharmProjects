from rich import print, inspect
from classd033 import *

def main():
    al = Aluno('Maria', 2000, "UI")
    al.idade = 30
    inspect(al, private=True, methods=True)


if __name__ == '__main__':
    main()