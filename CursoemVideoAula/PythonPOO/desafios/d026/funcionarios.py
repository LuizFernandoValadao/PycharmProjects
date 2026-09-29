from abc import ABC, abstractmethod

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    def __init__(self, nome, sal_bruto, salario):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    def analisar_sal(self):
        pass

    @abstractmethod
    def calc_sal(self):
        pass


class FuncionarioHorista(Funcionario, ABC):
    def __init__(self, nome, valor_hora, horas_trab, sal_bruto = 0, salario = 0):
        super().__init__(nome, sal_bruto, salario)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.salario = self.valor_hora * self.horas_trab
        return f'O salário de Paulo ()R${self.salario:.2f}'


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto, salario):
        super().__init__(nome, sal_bruto, salario)

    def calc_sal(self):
        pass