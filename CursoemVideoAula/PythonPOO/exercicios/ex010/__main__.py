from ex009 import*
from rich import print, inspect

def main():
    av1 = Avaliacao('pedro', 'Matemática', 9.5)
    av1.set_nota(25)
    inspect(av1, private=True)

if __name__ == '__main__':
    main()