from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome, sal):
        self.nome = nome
        self.__salario = sal

    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
    pass

class 