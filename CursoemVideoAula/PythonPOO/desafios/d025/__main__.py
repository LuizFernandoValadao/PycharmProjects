from transporte import *
from rich import print
from rich.table import Table

def main():
    dist = 20

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title='Tabela de Fretes', style='blue')

    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    tabela.add_row(f'{dist}Km', 'Moto', viagem[0].calcular_frete())
    tabela.add_row(f'{dist}Km', 'Caminhao', viagem[1].calcular_frete())
    tabela.add_row(f'{dist}Km', 'Drone', viagem[2].calcular_frete())

    print(tabela)


if __name__ == '__main__':
    main()