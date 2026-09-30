from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        self.conteudo = ''

    def analisar_sal(self):
        self.tnt_sal = self.salario / Funcionario.sal_min
        self.conteudo += f' e corresponde a [green]{self.tnt_sal:.1f} salários mínimos.[/]'
        panel = Panel(self.conteudo, title='Análise de Salário', width=50)
        print(panel)


    @abstractmethod
    def calc_sal(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        self.conteudo += f'O salário de [blue]{self.nome}[/] ([violet]FuncionarioHorista[/]) é de [green]R${self.salario:.2f}[/]'


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        self.conteudo += f'O salário de [blue]{self.nome}[/] ([violet]FuncionarioMensalista[/]) é de [green]R${self.salario:.2f}[/]'
