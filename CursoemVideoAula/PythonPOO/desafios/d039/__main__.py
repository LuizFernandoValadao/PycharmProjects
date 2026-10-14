from classes import *
from rich import print, inspect

def main():
   validar_dado(Usuario(), 'Guanabara123')
   validar_dado(Email(), 'gustavo@gmail.com')
   validar_dado(Senha(), 'Se3!')

if __name__ == '__main__':
    main()