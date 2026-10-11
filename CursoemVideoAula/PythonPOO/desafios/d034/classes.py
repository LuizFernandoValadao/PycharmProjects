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



class Gerente(Funcionario):
    bonus = 15

    def __init__(self, nome: str|None, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return (Gerente.bonus * self.salario / 100)

    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o Bônus será de {self.calcular_bonus()}'


class Designer(Funcionario):
    bonus = 8

    def __init__(self, nome: str|None, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return (Designer.bonus * self.salario / 100)

    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o Bônus será de {self.calcular_bonus()}'


class Desenvolvedor(Funcionario):
    bonus = 10

    def __init__(self, nome: str|None, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return (Desenvolvedor.bonus * self.salario / 100)

    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o Bônus será de {self.calcular_bonus()}'

