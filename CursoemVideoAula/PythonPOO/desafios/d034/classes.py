from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome: str|None = None, salario: float = 1621):
        self.nome = nome
        self.__salario = salario
        self.salario = self.__salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor: float):
        if valor < self.salario:
            raise ValueError('Você não pode reduzir o salário de um funcionário.')
        else:
            self.__salario = valor

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o Bônus será de {self.calcular_bonus():,.2f}'


class Gerente(Funcionario):

    def calcular_bonus(self):
        return 0.15 * self.salario


class Designer(Funcionario):

    def calcular_bonus(self):
        return 0.08 * self.salario


class Desenvolvedor(Funcionario):

    def calcular_bonus(self):
        return 0.1 * self.salario

