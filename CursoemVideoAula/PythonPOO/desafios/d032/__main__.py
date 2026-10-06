from conta_bancaria import *
from rich import print, inspect

def main():
    print("Criando a conta...")
    p = ContaBancaria(112, "Luiz", 1000, "Gafanhoto")

    print("Realizando depósito")
    p.depositar(500)

    print("Realizando saque")
    p.sacar(200)

    #inspect(p, private=True, methods=True)


if __name__ == '__main__':
    main()