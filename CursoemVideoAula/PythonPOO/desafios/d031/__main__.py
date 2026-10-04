from retangulo2 import *
from rich import print, inspect

def main():
    r = Retangulo()
    r.medidas = (4, 8)

    inspect(r, private=True, methods=True)
    print(r.medidas)

if __name__ == "__main__":
    main()