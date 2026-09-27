import math
from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perímetro(self)-> float:
        pass

    def area(self)-> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado


    def perímetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado * self.lado


class Círculo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perímetro(self):
        return self.raio * 2 * math.pi

    def area(self):
        return (self.raio * self.raio) * math.pi