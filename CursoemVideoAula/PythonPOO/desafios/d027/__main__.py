from personagem_rpg import *
from rich import inspect


def main():
    p1 = Guerreiro('Kratos', 1000)
    p2 = Mago("Gandalf", 2000)
    p1.atacar(p2, 200)
    p2.curar()




if __name__ == '__main__':
    main()